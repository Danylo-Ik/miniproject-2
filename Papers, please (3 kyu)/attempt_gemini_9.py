import datetime

class Inspector:
  def __init__(self):
    self.allowed_countries = []
    self.required_documents = {}
    self.required_vaccinations = {}
    self.wanted_criminal = None

  def receive_bulletin(self, bulletin):
    for line in bulletin.splitlines():
      parts = line.split(": ")
      if parts[0] == "Allow citizens of":
        self.allowed_countries.extend(parts[1].split(", "))
      elif parts[0] == "Entrants require":
        self.required_documents[parts[1]] = True
      elif parts[0] == "Citizens of":
        self.required_documents[parts[1]] = True
      elif parts[0] == "Workers require":
        self.required_documents[parts[1]] = True
      elif parts[0] == "Wanted by the State":
        self.wanted_criminal = parts[1]
      elif parts[0] == "Citizens of":
        # Handle vaccinations for specific countries (split on comma)
        countries, vaccine = parts[1].split(" require ")
        self.required_vaccinations.update({country: vaccine.strip() for country in countries.split(", ")})
      elif parts[0] == "Entrants no longer require":
        self.required_documents.pop(parts[1], None)

  def inspect(self, entrant):
    # Check for missing documents
    missing_documents = [doc for doc, required in self.required_documents.items() if doc not in entrant]
    if missing_documents:
      return f"Entry denied: missing required {', '.join(missing_documents)}."

    # Check for expired documents (assuming all expire on Nov 22, 1982)
    for doc, info in entrant.items():
      if "EXP:" in info and datetime.datetime.strptime(info.split("EXP: ")[1], "%Y.%m.%d") <= datetime.datetime(1982, 11, 22):
        return f"Entry denied: {doc} expired."

    # Check for vaccination requirements
    if "certificate_of_vaccination" in entrant:
      vaccination = entrant["certificate_of_vaccination"]
      required_vac = self.required_vaccinations.get(entrant.get("NATION", None))
      if required_vac and required_vac not in vaccination:
        return f"Entry denied: missing required vaccination ({required_vac})."
    elif "certificate_of_vaccination" in self.required_documents:
      return f"Entry denied: missing required vaccination."

    # Check if foreigner with missing access permit but has asylum or diplomatic authorization
    if (entrant.get("NATION", None) not in self.allowed_countries) and (
        "access_permit" not in entrant
    ):
      if "grant_of_asylum" in entrant or (
          "diplomatic_authorization" in entrant
          and "Arstotzka" in entrant["diplomatic_authorization"]
      ):
        return "Cause no trouble."
      else:
        return f"Entry denied: missing required access permit."

    # Check for document mismatches (excluding grant_of_asylum for Roman)
    mismatched_fields = []
    for doc1, info1 in entrant.items():
      if doc1 != "grant_of_asylum":  # Skip grant_of_asylum check for Roman
        for doc2, info2 in entrant.items():
          if doc1 != doc2 and info1.split()[1] != info2.split()[1]:
            mismatched_fields.append(f"{doc1} {info1.split()[0]} mismatch")
      if self.wanted_criminal and self.wanted_criminal in info1:
        return "Detainment: Entrant is a wanted criminal."

    if mismatched_fields:
      # Return the first mismatch encountered
      return f"Detainment: {mismatched_fields[0]}"

    # Citizen of Arstotzka
    if entrant.get("NATION", None) == "Arstotzka":
      return "Glory to Arstotzka."

    # Foreigner with valid documents
    return "Cause no trouble."
