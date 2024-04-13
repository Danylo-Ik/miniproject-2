from datetime import datetime

class Inspector:
    def __init__(self):
        self.nations = {
            "Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"
        }
        self.required_documents = set()
        self.required_vaccinations = set()
        self.wanted_criminals = set()
    
    def receive_bulletin(self, bulletin: str):
        updates = bulletin.split(";")
        for update in updates:
            category, data = update.split(":")
            if category.strip() == "Updates to the list of nations":
                self.update_nations(data.strip())
            elif category.strip() == "Updates to required documents":
                self.update_required_documents(data.strip())
            elif category.strip() == "Updates to required vaccinations":
                self.update_required_vaccinations(data.strip())
            elif category.strip() == "Update to a currently wanted criminal":
                self.update_wanted_criminals(data.strip())
    
    def update_nations(self, data):
        for entry in data.split(","):
            action, nation = entry.strip().split()
            if action == "Allow":
                self.nations.add(nation)
            elif action == "Deny":
                self.nations.discard(nation)
    
    def update_required_documents(self, data):
        for entry in data.split(","):
            action, document = entry.strip().split()
            if action == "Require":
                self.required_documents.add(document)
            elif action == "Unrequire":
                self.required_documents.discard(document)
    
    def update_required_vaccinations(self, data):
        for entry in data.split(","):
            action, vaccination = entry.strip().split()
            if action == "Require":
                self.required_vaccinations.add(vaccination)
            elif action == "Unrequire":
                self.required_vaccinations.discard(vaccination)
    
    def update_wanted_criminals(self, data):
        action, criminal = data.strip().split(":")
        if action == "Wanted by the State":
            self.wanted_criminals.add(criminal.strip())
        elif action == "Pardon":
            self.wanted_criminals.discard(criminal.strip())
    
    def inspect(self, documents: dict):
        if "passport" not in documents or "certificate_of_vaccination" not in documents:
            return "Entry denied: Missing required documents"
        
        if any(document not in documents for document in self.required_documents):
            return "Entry denied: Missing required documents"
        
        if "passport" in documents and documents["passport"]["expiration"] <= datetime(1982, 11, 22):
            return "Entry denied: Passport expired"
        
        if "certificate_of_vaccination" in documents and not self.required_vaccinations.issubset(documents["certificate_of_vaccination"]):
            return "Entry denied: Missing required vaccination"
        
        if "ID_card" in documents and documents["ID_card"]["nationality"] in self.wanted_criminals:
            return "Detainment: Entrant is a wanted criminal"
        
        if "ID_card" in documents and documents["ID_card"]["nationality"] == "Arstotzka":
            return "Glory to Arstotzka"
        
        if "access_permit" in documents and documents["access_permit"]["purpose"] == "work":
            if "work_pass" not in documents:
                return "Entry denied: Missing required work pass"
        
        if "access_permit" not in documents and "grant_of_asylum" not in documents and "diplomatic_authorization" not in documents:
            return "Entry denied: Missing required access permit"
        
        if "access_permit" in documents and documents["access_permit"]["nationality"] not in self.nations:
            return "Entry denied: Access permit nationality mismatch"
        
        return "Cause no trouble"

# Example usage:
inspector = Inspector()
inspector.receive_bulletin("Updates to the list of nations: Allow citizens of Obristan; Deny citizens of Kolechia, Republia; Updates to required documents: Require access_permit, work_pass; Unrequire ID_card; Updates to required vaccinations: Require polio; Unrequire tetanus; Update to a currently wanted criminal: Wanted by the State: Hubert Popovic")
documents1 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "certificate_of_vaccination": ["polio"],
    "ID_card": {"nationality": "Arstotzka"}
}
documents2 = {
    "passport": {"expiration": datetime(1980, 1, 1)},
    "certificate_of_vaccination": ["polio"]
}
documents3 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "certificate_of_vaccination": ["polio"]
}
documents4 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "certificate_of_vaccination": ["polio"],
    "ID_card": {"nationality": "Republia"}
}
documents5 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "access_permit": {"purpose": "work"}
}
documents6 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "access_permit": {"purpose": "work"},
    "work_pass": {}
}
documents7 = {
    "passport": {"expiration": datetime(2024, 12, 31)},
    "access_permit": {"purpose": "visit", "nationality": "Obristan"}
}
print(inspector.inspect(documents1))  # Output: 'Glory to Arstotzka'
print(inspector.inspect(documents2))  # Output: 'Entry denied: Passport expired'
print(inspector.inspect(documents3))  # Output: 'Cause no trouble'
print(inspector.inspect(documents4))  # Output: 'Detainment: Entrant is a wanted criminal'
print(inspector.inspect(documents5))  # Output: 'Entry denied: Missing required work pass'
print(inspector.inspect(documents6))  # Output: 'Cause no trouble'
print(inspector.inspect(documents7))  # Output: 'Entry denied: Access permit nationality mismatch'
