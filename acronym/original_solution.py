'''
This function takes the first letter of each word in a string and returns an acronym
'''
import timeit
from memory_profiler import memory_usage

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


test_code = lambda: create_acronym("Факультет Прикладних Наук Українського Католицького Університету")

sum_time = 0
sum_memory = 0
for i in range(100):
    start_time = timeit.default_timer()
    start_memory = memory_usage()[0]
    test_code()
    end_time = timeit.default_timer()
    end_memory = memory_usage()[0]
    execution_time = end_time - start_time
    memory_used = end_memory - start_memory
    sum_time += execution_time
    sum_memory += memory_used

print(f"Average execution time: {sum_time/100} seconds")
print(f"Average memory used: {sum_memory/100} MB")
