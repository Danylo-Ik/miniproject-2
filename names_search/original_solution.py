'''working with names'''
import timeit, memory_profiler

def read_file(file_path):
    '''reads file and returns dictionary of names, where key is number 
    of people with this name, and value is list of names'''
    names = {}
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            line = line.replace('\n', '').replace('(', '').replace(')', '')
            name = [line.split()[0]]
            count = int(line.split()[-1])
            if not line.isnumeric():
                dic = {count : name}
                if count not in names:
                    names.update(dic)
                else:
                    names[count].append(*name)
    return names

def most_popular_names(names):
    '''returns the set of most popular names'''
    temp = dict(names)

    most_popular = set()

    for _ in range(3):
        biggest = max(temp.keys())
        most_popular.add(*names[biggest])
        del temp[biggest]

    return most_popular

def appear_once(names):
    '''returns the tuple, first element is number of unique names, 
    second is a set of those names'''
    res = set()
    for name in names[1]:
        res.add(name)
    return tuple((len(names[1]), res))

def first_letter(names):
    '''returns the letter, that appears the most on the first position in names,
    number of different names, that start with it and number of children with this letter
    being first in their names'''
    letters_count = {}
    for children_count, lis in names.items():
        for name in lis:
            letter = name[0]
            if letter not in letters_count:
                letters_count.update({letter:[children_count, 1]})
            else:
                letters_count[letter][0] += children_count
                letters_count[letter][1] += 1

    max_key = max(letters_count, key = lambda x: letters_count[x][1])
    return tuple((max_key, letters_count[max_key][1], letters_count[max_key][0]))

def find_names(file_path):
    '''returnig the tuple of three needed functions'''
    names = read_file(file_path)

    return tuple((most_popular_names(names), appear_once(names), first_letter(names)))


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
