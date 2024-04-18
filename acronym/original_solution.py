'''
This function takes the first letter of each word in a string and returns an acronym
'''
import timeit

test_code = """
def create_acronym(message: str) -> str:
    if not isinstance(message, str):
        return None

    acronym = ""
    sentences = message.split('\\n')

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if not word.isalpha():
                return None
            acronym += word[0].upper()
        acronym += ' - ' + sentence
        if sentence != sentences[-1]:
            acronym += '\\n'

    return acronym

create_acronym("Факультет Прикладних Наук Українського Католицького Університету")
"""

if __name__ == '__main__':
    execution_time = timeit.timeit(stmt=test_code, number=1000)
    print(f"Execution time: {execution_time} seconds")
