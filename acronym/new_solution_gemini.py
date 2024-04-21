import timeit
from memory_profiler import memory_usage

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


# test_code = lambda: create_acronym("Факультет Прикладних Наук Українського Католицького Університету")

# sum_time = 0
# sum_memory = 0
# for i in range(100):
#     start_time = timeit.default_timer()
#     start_memory = memory_usage()[0]
#     test_code()
#     end_time = timeit.default_timer()
#     end_memory = memory_usage()[0]
#     execution_time = end_time - start_time
#     memory_used = end_memory - start_memory
#     sum_time += execution_time
#     sum_memory += memory_used

# print(f"Average execution time: {sum_time/100} seconds")
# print(f"Average memory used: {sum_memory/100} MB")
