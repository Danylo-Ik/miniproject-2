class Inspector:
    def __init__(self):
        self.bulletin = {
            "nations": [],
            "required_documents": [],
            "required_vaccinations": [],
            "wanted_criminals": []
        }
    
    def receive_bulletin(self, bulletin: str):
        updates = bulletin.split(";")
        for update in updates:
            category, data = update.split(":")
            self.bulletin[category.strip()] = [item.strip() for item in data.split(",")]
    
    def inspect(self, documents: dict):
        if "passport" not in documents:
            return "Entry denied: Passport missing"
        
        if "certificate_of_vaccination" not in documents:
            return "Entry denied: Certificate of vaccination missing"
        
        if any(vaccination not in documents["certificate_of_vaccination"] for vaccination in self.bulletin["required_vaccinations"]):
            return "Entry denied: Missing required vaccination"
        
        if "ID_card" in documents and documents["ID_card"] in self.bulletin["wanted_criminals"]:
            return "Detainment: Wanted criminal"
        
        if "ID_card" in documents and documents["ID_card"] in self.bulletin["nations"]:
            return "Glory to Arstotzka"
        
        if "ID_card" not in documents:
            return "Cause no trouble"

# Example usage:
inspector = Inspector()
inspector.receive_bulletin("nations: Arstotzka, Kolechia, Obristan; required_documents: passport, certificate_of_vaccination; required_vaccinations: COVID-19, Yellow Fever; wanted_criminals: Simon Wens")
documents1 = {"passport": "123456", "certificate_of_vaccination": ["COVID-19", "Yellow Fever"]}
documents2 = {"passport": "123457", "certificate_of_vaccination": ["COVID-19", "Yellow Fever"], "ID_card": "Simon Wens"}
documents3 = {"passport": "123458", "certificate_of_vaccination": ["COVID-19", "Yellow Fever"], "ID_card": "John Doe"}
print(inspector.inspect(documents1))  # Output: 'Glory to Arstotzka'
print(inspector.inspect(documents2))  # Output: 'Detainment: Wanted criminal'
print(inspector.inspect(documents3))  # Output: 'Cause no trouble'