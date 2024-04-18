@profile
def validate_board(board: list) -> bool:
    """
    list(str) -> bool
    >>> board = [\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"]
    >>> validate_board(board)
    False

    >>> board = [\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3      **",\
"  8  2***",\
"  2  ****"]
    >>> validate_board(board)
    True
    """
    lines = []
    rows = []
    #Check for repeats in lines
    for i in board:
        lines.append(list(i))
    for line in lines:
        for el in line:
            if el.isdigit():
                if line.count(el) > 1 or 0 > int(el) or int(el) > 10:
                    return False
    #Check for repeats in rows
    for i in range(len(lines[0])):
        row = []
        for line in lines:
            row.append(line[i])
        rows.append(row)
    for row in rows:
        for el in row:
            if el.isdigit():
                if row.count(el) > 1 or 0 > int(el) or int(el) > 10:
                    return False
    return check_colors(lines, rows)

@profile
def check_colors(lines: list, rows: list) -> bool:
    """
    Check for repeats in same colored tiles
    """
    start_line = 4
    start_row = 1
    i = 0
    j = 8
    colors = []
    while i < 5:
        colors.append(list(rows[i][start_line: start_line + 5]) + \
list(lines[j][start_row: start_row + 4]))
        start_line -= 1
        start_row += 1
        i += 1
        j -= 1
    for color in colors:
        for el in color:
            if el.isdigit():
                if color.count(el) > 1 or 0 > int(el) or int(el) > 10:
                    return False
    return True


if __name__ == '__main__':
    board1 = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   1  **",
    "  8  2***",
    "  2  ****"
]
    validate_board(board1)