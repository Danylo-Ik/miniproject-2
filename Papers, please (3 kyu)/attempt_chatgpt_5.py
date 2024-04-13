from datetime import datetime

class Inspector:
    def __init__(self):
        self.bulletin = {
            "allowed_nations": set(),
            "required_documents": set(),
            "required_vaccinations": set(),
            "wanted_criminal": None
        }

    def receiveBulletin(self, bulletin):
        updates = bulletin.split("\n")
        for update in updates:
            parts = update.split(" ")
            if parts[0] == "Allow":
                self.bulletin["allowed_nations"].add(parts[3])
            elif parts[0] == "Deny":
                self.bulletin["allowed_nations"].discard(parts[3])
            elif parts[1] == "require":
                self.bulletin["required_documents"].add(parts[0])
            elif parts[1] == "no" and parts[2] == "longer":
                self.bulletin["required_documents"].discard(parts[4])
            elif parts[1] == "require":
                self.bulletin["required_vaccinations"].add(parts[4])
            elif parts[1] == "no" and parts[2] == "longer":
                self.bulletin["required_vaccinations"].discard(parts[4])
            elif parts[0] == "Wanted":
                self.bulletin["wanted_criminal"] = parts[-1]

    def inspect(self, entrant):
        # Check if all required documents are present
        for document in self.bulletin["required_documents"]:
            if document not in entrant:
                return f"Entry denied: missing required {document.replace('_', ' ')}."

        # Check for mismatching information
        for key, value in entrant.items():
            if key != "passport" and key != "certificate_of_vaccination":
                if "nationality" in value and value["nationality"] not in self.bulletin["allowed_nations"]:
                    return f"Detainment: mismatching nationality found in {key}."

        # Check document expiration
        for key, value in entrant.items():
            if "expiration" in value:
                expiration_date = datetime.strptime(value["expiration"], "%Y.%m.%d")
                if expiration_date <= datetime(1982, 11, 22):
                    return f"Entry denied: {key.capitalize()} expired."

        # Check for wanted criminal
        if self.bulletin["wanted_criminal"] and any(self.bulletin["wanted_criminal"] in document.values() for document in entrant.values()):
            return "Detainment: Entrant is a wanted criminal."

        # Check vaccinations
        if "certificate_of_vaccination" in entrant:
            vaccinations = entrant["certificate_of_vaccination"].split(", ")
            for vaccine in self.bulletin["required_vaccinations"]:
                if vaccine not in vaccinations:
                    return f"Entry denied: missing required {vaccine} vaccination."

        # Check worker status
        if "access_permit" in entrant and entrant["access_permit"]["purpose"] == "work":
            if "work_pass" not in entrant:
                return "Entry denied: missing required work pass."

        # Check for Arstotzkan citizen or foreigner
        if "passport" in entrant and entrant["passport"]["nationality"] == "Arstotzka":
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."

# Test example
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector = Inspector()
inspector.receiveBulletin(bulletin)

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
