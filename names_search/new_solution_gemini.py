# import timeit, memory_profiler

def read_file(file_path):
  """Reads file and returns dictionary of names, where key is number
  of people with this name, and value is a list of names"""
  names = {}
  with open(file_path, 'r', encoding='UTF-8') as file:
    next(file, None)  # Skip the first line (if any)
    for line in file:
      name, count_str = line.strip().split(maxsplit=1)
      try:
        count = int(count_str)  # No parentheses removal, assuming consistent format
        names.setdefault(count, []).append(name)
      except ValueError:
        print(f"WARNING: Ignoring invalid count '{count_str}' in line: {line}")

  return names

def most_popular_names(names):
  """returns the set of most popular names"""
  if not names:
    return set()
  most_popular_count = max(names)
  return set(names[most_popular_count])

def appear_once(names):
  """returns the tuple, first element is number of unique names,
  second is a set of those names"""
  if not names:
    return 0, set()
  unique_names = set(names[1])
  return len(unique_names), unique_names

def first_letter(names):
  """returns the letter, that appears the most on the first position in names,
  number of different names, that start with it and number of children with this letter
  being first in their names"""
  letters_count = {}
  if not names:
    return None, None, None
  for children_count, name_list in names.items():
    for name in name_list:
      letter = name[0]
      letters_count.setdefault(letter, [0, 0])[0] += children_count
      letters_count[letter][1] += 1

  if not letters_count:
    return None, None, None  # Handle no names case
  max_letter, (max_count, _) = max(letters_count.items(), key=lambda x: x[1][1])
  return max_letter, max_count, letters_count[max_letter][0]

def find_names(file_path):
  """returning the tuple of three needed functions"""
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
