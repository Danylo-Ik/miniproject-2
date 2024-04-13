from datetime import datetime

class Inspector:
    def __init__(self):
        self.nations_allowed = []
        self.required_documents = {}
        self.required_vaccinations = []
        self.wanted_criminal = None

    def receive_bulletin(self, bulletin):
        lines = bulletin.split("\n")
        for line in lines:
            if line.startswith("Allow citizens of"):
                nations = line.replace("Allow citizens of", "").split(", ")
                self.nations_allowed.extend(nations)
            elif line.startswith("Deny citizens of"):
                nations = line.replace("Deny citizens of", "").split(", ")
                self.nations_allowed = [nation for nation in self.nations_allowed if nation not in nations]
            elif line.startswith("Foreigners require") or line.startswith("Citizens of") or line.startswith("Workers require"):
                parts = line.split(" require ")
                category = parts[0].strip()
                documents = parts[1].split(", ")
                self.required_documents[category] = documents
            elif line.startswith("Wanted by the State:"):
                self.wanted_criminal = line.replace("Wanted by the State:", "").strip()

    def inspect(self, entrant):
        if self.wanted_criminal and self.wanted_criminal in entrant.values():
            return "Detainment: Entrant is a wanted criminal"
        
        documents_present = set(entrant.keys())
        missing_documents = self.check_missing_documents(documents_present)
        if missing_documents:
            return f"Entry denied: missing required {missing_documents}"

        expired_documents = self.check_expired_documents(entrant)
        if expired_documents:
            return f"Entry denied: {expired_documents} expired"
        
        mismatch_info = self.check_info_mismatch(entrant)
        if mismatch_info:
            return f"Detainment: {mismatch_info} mismatch"

        required_vaccination = self.check_required_vaccination(entrant)
        if required_vaccination:
            return "Entry denied: missing required vaccination"
        
        if "ID_card" in entrant.keys() or "passport" in entrant.keys():  # Added condition to check for passport
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."

    def check_missing_documents(self, documents_present):
        for category, required_docs in self.required_documents.items():
            if category not in documents_present:
                return category.replace(" require", "")
        return None

    def check_expired_documents(self, entrant):
        for doc, details in entrant.items():
            if "EXP:" in details:
                exp_date = details.split("EXP:")[1].strip()
                exp_date = datetime.strptime(exp_date, "%Y.%m.%d")
                if exp_date <= datetime(1982, 11, 22):
                    return doc
        return None

    def check_info_mismatch(self, entrant):
        id_numbers = set()
        for doc, details in entrant.items():
            if doc == "ID_card" or doc == "passport":
                id_numbers.add(details.split("ID#:")[1].split()[0].strip())
        if len(id_numbers) > 1:
            return "ID number"
        return None

    def check_required_vaccination(self, entrant):
        if "certificate_of_vaccination" in entrant.keys():
            vaccinations = entrant["certificate_of_vaccination"].split(":")[1].strip().split(", ")
            for vaccine in vaccinations:
                if vaccine not in self.required_vaccinations:
                    return True
        return False
