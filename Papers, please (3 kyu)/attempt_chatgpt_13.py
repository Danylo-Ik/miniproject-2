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
        
        nationality = None
        for doc, details in entrant.items():
            if doc == "passport":
                nationality = details.split("NATION:")[1].split()[0].strip()
                break
        
        if nationality is None or nationality not in self.nations_allowed:
            return "Entry denied: missing required passport."

        for category, required_docs in self.required_documents.items():
            if category.startswith("Citizens of") and nationality in category:
                for doc in required_docs:
                    if doc not in entrant:
                        return f"Entry denied: missing required {doc}"
            elif category.startswith("Foreigners") and nationality not in category:
                for doc in required_docs:
                    if doc not in entrant:
                        return f"Entry denied: missing required {doc}"

        for doc, details in entrant.items():
            if "EXP:" in details:
                exp_date = details.split("EXP:")[1].strip()
                exp_date = datetime.strptime(exp_date, "%Y.%m.%d")
                if exp_date <= datetime(1982, 11, 22):
                    return f"Entry denied: {doc} expired"

        id_numbers = set()
        for doc, details in entrant.items():
            if doc == "ID_card" or doc == "passport":
                id_numbers.add(details.split("ID#:")[1].split()[0].strip())
        if len(id_numbers) > 1:
            return "Detainment: ID number mismatch"

        if "certificate_of_vaccination" in entrant.keys():
            vaccinations = entrant["certificate_of_vaccination"].split(":")[1].strip().split(", ")
            for vaccine in vaccinations:
                if vaccine not in self.required_vaccinations:
                    return "Entry denied: missing required vaccination"

        return "Glory to Arstotzka."
