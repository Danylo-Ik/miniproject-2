class Inspector:
  """
  An Inspector class that receives bulletins and inspects entrant documents based on Papers Please game.
  """
  def __init__(self):
    self.expected_documents = {}  # Dictionary to store expected documents for each country

  def receive_bulletin(self, bulletin):
    """
    Receives a bulletin string containing information about expected documents.

    Args:
      bulletin: A string containing the bulletin information.
    """
    # Extract information from the bulletin
    for line in bulletin.splitlines():
      parts = line.split(":")
      country = parts[0].strip()
      documents = parts[1].strip().split(",")
      self.expected_documents[country] = documents

  def inspect(self, entrant):
    """
    Inspects an entrant's documents based on the expected documents for their country.

    Args:
      entrant: A dictionary containing entrant information, including "country" and "documents" keys.

    Returns:
      A string indicating ALLOW or DENY based on the inspection result.
    """
    # Check if entrant's country is present in expected documents
    if entrant["country"] not in self.expected_documents:
      return "DENY - Entry not permitted for country: {}".format(entrant["country"])

    # Check if all expected documents are present
    for document in self.expected_documents[entrant["country"]]:
      if document not in entrant["documents"]:
        return "DENY - Missing document: {}".format(document)

    # All documents are present and valid
    return "ALLOW"

# Example usage
inspector = Inspector()
bulletin = """Arstotzka: Passport, Work Permit
United Federation: Passport, Entry Permit
Kolechia: Passport, Ministry Pass"""
inspector.receive_bulletin(bulletin)

entrant1 = {"country": "Arstotzka", "documents": ["Passport", "Work Permit", "Extra Document"]}
entrant2 = {"country": "Arstotzka", "documents": ["Passport"]}
entrant3 = {"country": "Kolechia", "documents": ["Passport", "Ministry Pass"]}

print(inspector.inspect(entrant1))  # Output: ALLOW
print(inspector.inspect(entrant2))  # Output: DENY - Missing document: Work Permit
print(inspector.inspect(entrant3))  # Output: ALLOW
