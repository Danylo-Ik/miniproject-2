import timeit
@profile
def validate_board1(board: list) -> bool:
    """
    list(str) -> bool

    Checks if a Sudoku board is valid.

    >>> board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   1  **",
    "  8  2***",
    "  2  ****"]
    >>> validate_board(board)
    False

    >>> board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3      **",
    "  8  2***",
    "  2  ****"]
    >>> validate_board(board)
    True
    """

    lines = [list(i) for i in board]  # Create lines using list comprehension
    rows = [[line[i] for line in lines] for i in range(len(lines[0]))]  # Create rows using list comprehension

    # Combine digit check for lines and rows
    for data in lines + rows:
        for el in data:
            if el.isdigit():
                if data.count(el) > 1 or 0 > int(el) or int(el) > 10:
                    return False
    return check_colors1(lines, rows)

def check_colors1(lines: list, rows: list) -> bool:
    """
    Check for repeats in same colored tiles
    """
    start_line = 4
    start_row = 1
    i = 0
    j = 8
    colors = []
    while i < 5:
        colors.append(list(rows[i][start_line: start_line + 5]) + list(lines[j][start_row: start_row + 4]))
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

# Proposed grade: 0.48/1 but technically 1/1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: OK


@profile
def validate_board2(board: list) -> bool:
    """
    list(str) -> bool
    
    Checks if a Sudoku board is valid.
    
    >>> board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   1  **",
    "  8  2***",
    "  2  ****"]
    >>> validate_board(board)
    False
    
    >>> board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3      **",
    "  8  2***",
    "  2  ****"]
    >>> validate_board(board)
    True
    """
    
    # Combine line and row creation with digit validation
    data = [[c for c in row if c.isdigit() and (0 < int(c) <= 10 and data.count(c) < 1)] for row in board]
    if any(len(row) != 9 for row in data):  # Early return for missing digits
        return False
    
    # Check for repeats within sub-grids (improved clarity)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [data[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if any(subgrid.count(c) > 1 for c in subgrid):
                return False
    
    return True

# Proposed grade: 0/1
# Test1: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test2: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test3: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test4: Failed puzzle.validate_board([
# Test5: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test6: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test7: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test8: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35
# Test9: Failed puzzle.validate_board([
# cannot access free variable 'data' where it is not associated with a value in enclosing scope on line 35


@profile
def validate_board3(board: list) -> bool:
    # Convert board to sets for efficient duplicate checking
    rows = [set(row.replace(" ", "")) for row in board]
    cols = [set(col) for col in zip(*board)]
    subgrids = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            subgrids[i // 3 * 3 + j // 3].add(board[i][j])
    
    # Check for duplicates (excluding empty spaces)
    for row, col, subgrid in zip(rows, cols, subgrids):
        if len(row - {''}) != 9 or len(col - {''}) != 9 or len(subgrid - {''}) != 9:
            return False
    return True

# Proposed grade: 0.26/1
# Test1: OK
# Test2: OK
# Test3: Failed puzzle.validate_board([
# Test4: Failed puzzle.validate_board([
# Test5: Failed puzzle.validate_board([
# Test6: Failed puzzle.validate_board([
# Test7: OK
# Test8: OK
# Test9: OK


@profile
def validate_board4(board: list) -> bool:
    # Function to check if a set has all digits from 1 to 9 (excluding spaces)
    def has_all_digits(s):
        return s == set("123456789") - {''}
    
    # Convert board to rows and columns using list comprehension
    rows = [set(row.replace(" ", "")) for row in board]
    cols = [set(col) for col in zip(*board)]
    
    # Create subgrids using nested loops and string slicing
    subgrids = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            subgrids[i // 3 * 3 + j // 3].update(board[i][j * 3:j * 3 + 3])
    
    # Check for duplicates (excluding empty spaces)
    for row, col, subgrid in zip(rows, cols, subgrids):
        if not (has_all_digits(row) and has_all_digits(col) and has_all_digits(subgrid)):
            return False
    return True

# Proposed grade: 0.25/1
# Test1: OK
# Test2: OK
# Test3: Failed puzzle.validate_board([
# Test4: Failed puzzle.validate_board([
# Test5: Failed puzzle.validate_board([
# Test6: Failed puzzle.validate_board([
# Test7: OK
# Test8: OK
# Test9: OK

@profile
def validate_board5(board: list) -> bool:
    # Function to check if a set has all digits from 1 to 9 (excluding spaces)
    def has_all_digits(s):
        return s == set("123456789") - {''}
    
    # Check for invalid characters and missing digits
    for row in board:
        if len(row.replace(" ", "")) != 9 or not all(c.isdigit() or c == " " for c in row):
            return False
    
    # Convert board to rows and columns using list comprehension
    rows = [set(row.replace(" ", "")) for row in board]
    cols = [set(col) for col in zip(*board)]
    
    # Create subgrids using nested loops and string slicing
    subgrids = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            subgrids[i // 3 * 3 + j // 3].update(board[i][j * 3:j * 3 + 3])
    
    # Check for duplicates (excluding empty spaces)
    for row, col, subgrid in zip(rows, cols, subgrids):
        if not (has_all_digits(row) and has_all_digits(col) and has_all_digits(subgrid)):
            return False
    return True

# Proposed grade: 0.25/1
# Test1: OK
# Test2: OK
# Test3: Failed puzzle.validate_board([
# Test4: Failed puzzle.validate_board([
# Test5: Failed puzzle.validate_board([
# Test6: Failed puzzle.validate_board([
# Test7: OK
# Test8: OK
# Test9: OK


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
    "  2  ****"]
    # validate_board1(board1)
    # validate_board2(board1)
    # validate_board3(board1)
    # validate_board4(board1)
    # validate_board5(board1)
    
    