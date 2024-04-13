from datetime import datetime

class Inspector:
    def __init__(self):
        self.allowed_nations = set()
        self.required_documents = set()
        self.required_vaccinations = set()
        self.wanted_criminal = None

    def receive_bulletin(self, bulletin):
        updates = bulletin.split('\n')
        for update in updates:
            if update.startswith('Allow'):
                self.allowed_nations.update(update.split(' ')[-1].split(', '))
            elif update.startswith('Deny'):
                self.allowed_nations.difference_update(update.split(' ')[-1].split(', '))
            elif 'require' in update:
                if 'access permit' in update:
                    self.required_documents.add('access_permit')
                elif 'work pass' in update:
                    self.required_documents.add('work_pass')
                elif 'ID card' in update:
                    self.required_documents.add('ID_card')
                elif 'polio vaccination' in update:
                    self.required_vaccinations.add('polio')
                elif 'tetanus vaccination' in update:
                    self.required_vaccinations.discard('tetanus')
            elif 'Wanted by the State' in update:
                self.wanted_criminal = update.split(': ')[-1]

    def inspect(self, entrant):
        # Check for wanted criminal
        if self.wanted_criminal:
            for document in entrant.values():
                if isinstance(document, dict) and self.wanted_criminal in document.values():
                    return "Detainment: Entrant is a wanted criminal."

        # Check for missing or expired documents
        for doc_type in self.required_documents:
            if doc_type not in entrant:
                return f"Entry denied: missing required {doc_type.replace('_', ' ')}"
            elif 'expiration' in entrant[doc_type]:
                expiration_date = datetime.strptime(entrant[doc_type]['expiration'], "%Y.%m.%d")
                if expiration_date <= datetime(1982, 11, 22):
                    return f"Entry denied: {doc_type.replace('_', ' ')} expired"

        # Check for mismatching information
        for key, value in entrant.items():
            if isinstance(value, dict):
                if key == 'passport' and value.get('NATION') not in self.allowed_nations:
                    return "Detainment: Mismatching nationality found in passport."
                elif key == 'ID_card' and value.get('NATION') != 'Arstotzka':
                    return "Detainment: Mismatching nationality found in ID card."

        # Check for missing vaccinations
        if 'certificate_of_vaccination' in entrant:
            for vaccine in self.required_vaccinations:
                if vaccine not in entrant['certificate_of_vaccination'].get('vaccinations', []):
                    return f"Entry denied: missing required {vaccine} vaccination"

        # If all checks passed, determine the result
        if 'passport' in entrant and entrant['passport'].get('NATION') == 'Arstotzka':
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
        "NATION": "Arstotzka",
        "NAME": "Guyovich, Russian",
        "DOB": "1933.11.28",
        "SEX": "M",
        "ISS": "East Grestin",
        "EXP": "1983.07.10"
    }
}

print(inspector.inspect(entrant1))  # Output: 'Glory to Arstotzka.'
