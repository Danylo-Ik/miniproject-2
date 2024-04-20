# import timeit, memory_profiler
from collections import defaultdict

def read_file(file_path):
    '''Reads file and returns dictionary of names, where key is number 
    of people with this name, and value is list of names'''
    names = defaultdict(list)
    with open(file_path, 'r', encoding='UTF-8') as file:
        next(file)  # Skip the header line
        for line in file:
            name, count = line.strip().split('\t')
            names[int(''.join(filter(str.isdigit, count)))].append(name.strip())
    return names

def most_popular_names(names):
    '''Returns the set of most popular names'''
    sorted_names = sorted(names.items(), reverse=True)
    return {name for _, name_list in sorted_names[:3] for name in name_list}

def appear_once(names):
    '''Returns the tuple, first element is number of unique names, 
    second is a set of those names'''
    unique_names = {name for name, count in names.items() if len(count) == 1}
    return len(unique_names), unique_names

def first_letter(names):
    '''Returns the letter that appears the most on the first position in names,
    number of different names that start with it, and number of children with this letter
    being first in their names'''
    letters_count = defaultdict(lambda: [0, 0])
    for children_count, name_list in names.items():
        for name in name_list:
            first_letter = name[0]
            letters_count[first_letter][0] += 1
            letters_count[first_letter][1] += children_count
    max_key = max(letters_count, key=lambda x: letters_count[x][1])
    return max_key, letters_count[max_key][0], letters_count[max_key][1]

def find_names(file_path):
    '''Returns the tuple of three needed functions'''
    names = read_file(file_path)
    return most_popular_names(names), appear_once(names), first_letter(names)


# test_code = lambda: find_names('names.txt')

# sum_time = 0
# sum_memory = 0
# for i in range(100):
#     start_time = timeit.default_timer()
#     start_memory = memory_profiler.memory_usage()[0]
#     test_code()
#     end_time = timeit.default_timer()
#     end_memory = memory_profiler.memory_usage()[0]
#     execution_time = end_time - start_time
#     memory_used = end_memory - start_memory
#     sum_time += execution_time
#     sum_memory += memory_used

# print(f"Average execution time: {sum_time/100} seconds")
# print(f"Average memory used: {sum_memory/100} MB")
