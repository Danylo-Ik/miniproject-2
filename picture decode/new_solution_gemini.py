''' Picture decode '''
from typing import Dict

def read_file(path: str) -> dict:
    """
    Read file and return a dictionary {symbol: coordinates, ...}
    """
    res = {}
    symbol = None  # Initialize
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove trailing whitespace
            if not line:
                continue  # Skip empty lines

            # Check if line starts with a symbol (no leading whitespace)
            if not line[0].isdigit():
                symbol = line
            else:
                # Assume line contains coordinates
                value_str = line.strip()
                value_lst = [(int(x), int(y)) for x, y in (i.split('_') for i in value_str.split() if '_' in i)]

                # Assign the coordinates to the last read symbol
                if symbol is not None:
                    res[symbol] = value_lst
                    symbol = None  # Reset symbol for the next one

    return res


def save_pict_to_file(symbols: Dict, textfile: str) -> None:
    """
    Transforms a dictionary mapping symbols to coordinates into a text picture and writes it to a file.

    Args:
        symbols: Dictionary mapping symbols to a list of coordinate tuples (x, y).
        textfile: Path to the output file.

    Example Usage:
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
    """
    max_x, max_y = 0, 0
    for value in symbols.values():
        for x, y in value:
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    matrix = [[' '] * (max_y + 1) for _ in range(max_x + 1)] # Use list comprehension for efficiency
    for key, value in symbols.items():
        for x, y in value:
            matrix[x][y] = key

    with open(textfile, 'w', encoding='utf-8') as file:
        string = '\n'.join(''.join(row) for row in matrix)  # Efficient string construction
        file.write(string)


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