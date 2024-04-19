def create_acronym(message: str) -> str:
    """Creates an acronym from the first letter of each word in each sentence.

    Args:
        message: The message to create acronyms for.

    Returns:
        A string containing the acronyms for each sentence, separated by newlines.
        Returns None if the message is not a string or contains non-alphanumeric characters.
    """
    if not isinstance(message, str):
        return None

    acronyms = ""
    sentences = message.splitlines()

    for sentence in sentences:
        if not all(char.isalnum() or char.isspace() for char in sentence):
            return None

        acronym = ""
        for word in sentence.split():
            if not word:  # Handle empty words
                continue
            acronym += word[0].upper()

        acronyms += acronym + " - " + sentence.strip() + "\n"

    return acronyms[:-1]  # Remove trailing newline

print(create_acronym("Факультет Прикладних Наук Українського Католицького Університету"))