''' Picture decode '''
from typing import Dict

def read_file(path: str) -> Dict[str, list]:
    '''
    Read file and return a dictionary {symbol: coordinates, ...}
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding='utf-8') as tmp:
    ...    _=tmp.write("♥\\n0_0 1_1 2_2\\n%\\n0_1 0_2 1_2")
    >>> read_file(tmp.name)
    {'♥': [(0, 0), (1, 1), (2, 2)], '%': [(0, 1), (0, 2), (1, 2)]}
    '''
    res = {}
    with open(path, 'r', encoding='utf-8') as file:
        lines = (line.strip() for line in file)
        for key, value in zip(lines, lines):
            value_str = value.replace('_', ',')
            value_lst = [tuple(map(int, i.split(','))) for i in value_str.split()]
            res[key] = value_lst
    return res

def save_pict_to_file(symbols: Dict[str, list], textfile: str) -> None:
    '''Transform keys and values from dictionary into a txt picture, then write it in a file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('')
    >>> save_pict_to_file({'♥': [(0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 3), (1, 6),\
 (2, 1), (2, 5), (3, 2), (3, 4), (4, 3)]},tmp.name)
    >>> with open(tmp.name,"r",encoding="utf-8") as file:
    ...     print(file.read())
     ♥♥ ♥♥ 
    ♥  ♥  ♥
     ♥   ♥ 
      ♥ ♥  
       ♥   
    '''
    max_x, max_y = max(x for _, values in symbols.items() for x, _ in values), \
                   max(y for _, values in symbols.items() for _, y in values)

    matrix = [[' '] * (max_y + 1) for _ in range(max_x + 1)]
    for key, value in symbols.items():
        for x, y in value:
            matrix[x][y] = key

    with open(textfile, 'w', encoding='utf-8') as file:
        file.write('\n'.join(''.join(row) for row in matrix))


# import timeit
# from memory_profiler import memory_usage

# test_code = lambda: save_pict_to_file(read_file("picture.txt"), "output.txt")

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

# print(f"Average execution time: {(sum_time*1000)/100} ms")
# print(f"Average memory used: {sum_memory/100} MB")

