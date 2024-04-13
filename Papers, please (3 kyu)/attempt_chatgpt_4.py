from datetime import datetime

class Inspector:
    def __init__(self):
        self.bulletin = {
            "nations": set(),
            "required_documents": set(),
            "required_vaccinations": set(),
            "wanted_criminals": set()
        }
        self.allowed_countries = {"Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"}

    def receive_bulletin(self, bulletin: str):
        updates = bulletin.split("\n")
        for update in updates:
            parts = update.split(" ")
            if parts[0] == "Allow":
                self.bulletin["nations"].add(parts[3])
            elif parts[0] == "Deny":
                self.bulletin["nations"].discard(parts[3])
            elif parts[1] == "require":
                self.bulletin["required_documents"].add(parts[2])
            elif parts[1] == "no" and parts[2] == "longer":
                self.bulletin["required_documents"].discard(parts[4])
            elif parts[1] == "require":
                self.bulletin["required_vaccinations"].add(parts[4])
            elif parts[1] == "no" and parts[2] == "longer":
                self.bulletin["required_vaccinations"].discard(parts[4])
            elif parts[0] == "Wanted":
                self.bulletin["wanted_criminals"].add(parts[3])

    def inspect(self, entrant):
        # Check if all required documents are present
        for document in self.bulletin["required_documents"]:
            if document not in entrant:
                return f"Entry denied: Missing required {document.replace('_', ' ')}."

        # Check for conflicting information
        for key, value in entrant.items():
            if key != "passport" and key != "certificate_of_vaccination":
                if "nationality" in value and value["nationality"] not in self.bulletin["nations"]:
                    return f"Detainment: Mismatching nationality found in {key}."
        
        # Check document expiration
        for key, value in entrant.items():
            if "expiration" in value:
                expiration_date = datetime.strptime(value["expiration"], "%Y.%m.%d")
                if expiration_date <= datetime(1982, 11, 22):
                    return f"Entry denied: {key.capitalize()} expired."

        # Check for wanted criminals
        for key, value in entrant.items():
            if "nationality" in value and value["nationality"] in self.bulletin["wanted_criminals"]:
                return "Detainment: Entrant is a wanted criminal."

        # Check vaccinations
        if "certificate_of_vaccination" in entrant:
            vaccinations = entrant["certificate_of_vaccination"]["vaccinations"]
            for vaccine in self.bulletin["required_vaccinations"]:
                if vaccine not in vaccinations:
                    return f"Entry denied: Missing required {vaccine} vaccination."

        # Check for Arstotzkan citizen or foreigner
        if "passport" in entrant and entrant["passport"]["nationality"] == "Arstotzka":
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."

# Test example
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""
inspector = Inspector()
inspector.receive_bulletin(bulletin)

entrant1 = {
    "passport": {
        "ID": "GC07D-FU8AR",
        "nationality": "Arstotzka",
        "name": "Guyovich, Russian",
        "DOB": "1933.11.28",
        "sex": "M",
        "ISS": "East Grestin",
        "expiration": "1983.07.10"
    }
}
print(inspector.inspect(entrant1))  # Output: 'Glory to Arstotzka.'