class Inspector:
    def __init__(self):
        self.bulletin = {
            "allowed_countries": set(),
            "required_documents": set(),
            "required_vaccinations": set(),
            "wanted_criminal": None
        }

    def receive_bulletin(self, bulletin):
        lines = bulletin.split('\n')
        for line in lines:
            if "Allow citizens of" in line:
                countries = line.split("Allow citizens of ")[1].split(", ")
                self.bulletin["allowed_countries"].update(countries)
            elif "Deny citizens of" in line:
                countries = line.split("Deny citizens of ")[1].split(", ")
                self.bulletin["allowed_countries"].difference_update(countries)
            elif "require" in line:
                if "vaccination" in line:
                    self.bulletin["required_vaccinations"].update(line.split(": ")[1].split(", "))
                else:
                    self.bulletin["required_documents"].add(line.split("require ")[1])
            elif "Wanted by the State" in line:
                self.bulletin["wanted_criminal"] = line.split(": ")[1]

    def inspect(self, entrant):
        # Check for wanted criminal
        if self.bulletin["wanted_criminal"] in entrant.values():
            return "Detainment: Entrant is a wanted criminal"

        # Check for required documents
        for doc in self.bulletin["required_documents"]:
            if doc not in entrant:
                return f"Entry denied: missing required {doc.replace('_', ' ')}"

        # Check for required vaccinations
        for vacc in self.bulletin["required_vaccinations"]:
            if "certificate_of_vaccination" not in entrant:
                return "Entry denied: missing required vaccination"
            elif vacc not in entrant["certificate_of_vaccination"]:
                return "Entry denied: missing required vaccination"

        # Check expiration date
        for document, details in entrant.items():
            if "EXP" in details and details.split("EXP: ")[1] <= "1982.11.22":
                return "Entry denied: passport expired"

        # Check for mismatching information
        for key in entrant.keys():
            if key != "passport":
                if entrant[key] != entrant["passport"]:
                    return f"Detainment: {key.replace('_', ' ')} mismatch"

        # Check for citizenship
        if "passport" in entrant:
            if entrant["passport"].split("NATION: ")[1].split("\n")[0] == "Arstotzka":
                return "Glory to Arstotzka."
            elif entrant["passport"].split("NATION: ")[1].split("\n")[0] in self.bulletin["allowed_countries"]:
                return "Cause no trouble."

        return "Entry denied: Invalid entry"


# Test your implementation with the provided test cases
inspector = Inspector()
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector.receive_bulletin(bulletin)

josef = {
    "passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
}
guyovich = {
    "access_permit": 'NAME: Guyovich, Russian\nNATION: Obristan\nID#: TE8M1-V3N7R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 159cm\nWEIGHT: 60kg\nEXP: 1983.07.13'
}
roman = {
    "passport": 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
    "grant_of_asylum": 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'
}

print(inspector.inspect(josef))  # 'Glory to Arstotzka.'
print(inspector.inspect(guyovich))  # 'Entry denied: missing required passport.'
print(inspector.inspect(roman))  # 'Detainment: ID number mismatch.'
