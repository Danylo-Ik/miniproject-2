'''
Picture decode
 - 0.105 seconds
 - 0.003 MB
'''
from typing import Dict, TextIO

def read_file(path: str) -> dict:
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
        lst = file.read().split('\n')

    while '' in lst:
        lst.remove('')

    for i in range(len(lst) // 2):
        key = lst[i * 2]
        value_str = lst[i * 2 + 1].replace('_', ',')
        value_lst = [tuple(map(int, i.split(','))) for i in value_str.split()]
        res[key] = value_lst

    return res

def save_pict_to_file(symbols: Dict, textfile: str) -> TextIO:
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
    max_x, max_y = 0, 0
    for key, value in symbols.items():
        for i in value:
            x, y = i
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    matrix = [[' '] * (max_y + 1) for i in range(max_x + 1)]
    for key, value in symbols.items():
        for i in value:
            x, y = i
            matrix[x][y] = key

    with open(textfile, 'w', encoding='utf-8') as file:
        string = ''
        for i in matrix:
            string += ''.join(i)
            if matrix.index(i) != len(matrix) - 1:
                string += '\n'
        file.write(string)
