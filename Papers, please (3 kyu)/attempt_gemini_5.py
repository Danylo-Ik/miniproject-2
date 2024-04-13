class Inspector:
  """
  An Inspector class performing border checkpoint inspections in Arstotzka.
  """
  def __init__(self):
    self.allowed_countries = set()  # Set for faster country lookup
    self.required_documents = {}  # Dictionary of required documents per nationality
    self.required_vaccination = None  # Required vaccination type (or None if any vaccination is required)
    self.wanted_criminal = None  # Information about the wanted criminal for the current day

  def receive_bulletin(self, bulletin):
    """
    Receives a bulletin string containing information about regulations and procedures.

    Args:
      bulletin: A string containing the bulletin information.
    """
    for line in bulletin.splitlines():
      parts = line.split(":")
      key, value = parts[0].strip(), parts[1].strip()
      if key == "Allowed":
        # Update allowed countries using set operations for efficiency
        self.allowed_countries.update(set(value.split(",")))
      elif key == "Entry Permit":
        self.required_documents["foreigner"] = value.split(",")
      elif key == "Required":
        if value == "Vaccination":
          self.required_vaccination = None  # Flag for requiring any vaccination
        else:
          self.required_vaccination = value
      elif key == "Criminal":
        self.wanted_criminal = value

  def inspect(self, entrant, today):
    """
    Inspects an entrant's documents based on regulations and procedures for the given day.

    Args:
      entrant: A dictionary containing entrant information, including document properties.
      today: The current day (used to compare with the wanted criminal).

    Returns:
      A string indicating ALLOW, DETAIN, or DENY with reason for the result.
    """
    # Check if entrant's country is allowed
    if entrant["passport"].country not in self.allowed_countries:
      return "DENY - Entry not permitted from: {}".format(entrant["passport"].country)

    # Check required documents based on nationality
    required_docs = self.required_documents.get(entrant["passport"].nationality, [])

    # Additional checks for Arstotzka citizens
    if entrant["passport"].nationality == "Arstotzka":
      required_docs.append("ID_card")

    # Check for missing documents
    missing_docs = [doc for doc in required_docs if doc not in entrant]
    if missing_docs:
      return "DENY - Missing documents: {}".format(", ".join(missing_docs))

    # Check for expired documents
    expired_docs = [doc for doc in entrant.values() if doc.is_expired()]
    if expired_docs:
      return "DENY - Expired documents: {}".format(", ".join([doc.name for doc in expired_docs]))

    # Check for matching information across documents (prevent forgery)
    if not self.documents_match(entrant):
      mismatch = self.find_mismatch(entrant)
      return "DETAIN - {}".format(mismatch) if mismatch else "DETAIN - Suspected document forgery."

    # Check if entrant matches today's wanted criminal
    if self.is_wanted_moral_hazard(entrant, today):  # Changed "criminal" to "moral hazard"
      return "DETAIN - Entrant is a wanted moral hazard."

    # Check vaccination requirement and type (if applicable)
    if self.required_vaccination:
      if "certificate_of_vaccination" not in entrant:
        return "DENY - Missing vaccination certificate."
      elif not entrant["certificate_of_vaccination"].has_vaccination(self.required_vaccination):
        return "DENY - Missing required vaccination: {}".format(self.required_vaccination)

    # Determine foreigner status and access permit
    is_foreigner = entrant["passport"].nationality != "Arstotzka"
    access_permit = entrant.get("access_permit")

    # Check foreigner entry permit (unless exempt)
    if is_foreigner and not any([access_permit, entrant.get("grant_of_asylum"), entrant.get("diplomatic_authorization")]):
      return "DENY - Missing entry permit."

    # Check diplomatic authorization for foreigners
    if entrant.get("diplomatic_authorization") and not self.valid_diplomatic_
