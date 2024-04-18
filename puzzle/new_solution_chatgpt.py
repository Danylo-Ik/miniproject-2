import timeit

@profile
def validate_board1(board: list) -> bool:
    # Function to check if a given sequence has any repeated digits
    def has_repeated_digits(seq: str) -> bool:
        seen = set()
        for char in seq:
            if char.isdigit():
                if char in seen:
                    return True
                seen.add(char)
        return False

    # Check rows and columns for repeated digits
    for row in board:
        if has_repeated_digits(row):
            return False
    for col in zip(*board):
        if has_repeated_digits(col):
            return False

    # Check colors for repeated digits
    for i in range(5):
        color = ''.join(board[i][4-j] + board[8-j][i] for j in range(5))
        if has_repeated_digits(color):
            return False

    return True

# Proposed grade: 0.37 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: Failed puzzle.validate_board([
# Test6: Failed puzzle.validate_board([
# Test7: OK
# Test8: OK
# Test9: OK


@profile
def validate_board2(board: list) -> bool:
    # Function to check if a given sequence has any repeated digits
    def has_repeated_digits(seq: str) -> bool:
        seen = set()
        for char in seq:
            if char.isdigit():
                if char in seen:
                    return True
                seen.add(char)
        return False

    # Check rows and columns for repeated digits
    for row in board:
        if has_repeated_digits(row):
            return False
    for col in zip(*board):
        if has_repeated_digits(col):
            return False

    # Check colors for repeated digits
    for i in range(5):
        color1 = ''.join(board[i][4-j] for j in range(5))
        color2 = ''.join(board[8-j][i] for j in range(5))
        if has_repeated_digits(color1) or has_repeated_digits(color2):
            return False

    return True

# Proposed grade: 0.43 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: Failed puzzle.validate_board([


@profile
def validate_board3(board: list) -> bool:
    seen_rows = [set() for _ in range(9)]
    seen_cols = [set() for _ in range(9)]
    seen_colors = [set() for _ in range(10)]

    for i in range(9):
        for j in range(9):
            char = board[i][j]
            if char.isdigit():
                # Check row
                if char in seen_rows[i]:
                    return False
                seen_rows[i].add(char)
                # Check column
                if char in seen_cols[j]:
                    return False
                seen_cols[j].add(char)
                # Check color
                color_idx = 3 * (i // 3) + (j // 3)
                if char in seen_colors[color_idx]:
                    return False
                seen_colors[color_idx].add(char)

    return True

# Proposed grade: 0.43 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: Failed puzzle.validate_board([


@profile
def validate_board4(board: list) -> bool:
    seen_rows = [set() for _ in range(9)]
    seen_cols = [set() for _ in range(9)]
    seen_colors = [set() for _ in range(10)]

    for i in range(9):
        for j in range(9):
            char = board[i][j]
            if char.isdigit():
                color_idx = 3 * (i // 3) + (j // 3)
                if char in seen_rows[i] or char in seen_cols[j] or char in seen_colors[color_idx]:
                    return False
                seen_rows[i].add(char)
                seen_cols[j].add(char)
                seen_colors[color_idx].add(char)

    return True

# Proposed grade: 0.42 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: Failed puzzle.validate_board([


@profile
def validate_board5(board: list) -> bool:
    for i in range(9):
        for j in range(9):
            char = board[i][j]
            if char.isdigit():
                # Check row
                if board[i].count(char) > 1:
                    return False
                # Check column
                if [board[x][j] for x in range(9)].count(char) > 1:
                    return False
                # Check color
                color_start_row, color_start_col = 3 * (i // 3), 3 * (j // 3)
                if [board[x][y] for x in range(color_start_row, color_start_row + 3) for y in range(color_start_col, color_start_col + 3)].count(char) > 1:
                    return False
    return True

# Proposed grade: 0.42 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: Failed puzzle.validate_board([



@profile
def validate_board6(board: list) -> bool:
    """
    Validate the Sudoku board.
    """
    def check_duplicates(data):
        """
        Check for duplicates in data.
        """
        for line in data:
            numbers = [c for c in line if c.isdigit()]
            for num in numbers:
                if numbers.count(num) > 1 or not (1 <= int(num) <= 9):
                    return False
        return True

    def extract_colors():
        """
        Extract tiles of the same color.
        """
        colors = []
        for i in range(4):
            colors.append([board[j][4-i] for j in range(5-i)] + [board[8-j][i] for j in range(4-i)])
        return colors

    lines = board
    rows = [''.join([board[j][i] for j in range(9)]) for i in range(9)]

    if not (check_duplicates(lines) and check_duplicates(rows)):
        return False

    colors = extract_colors()
    for color in colors:
        if not check_duplicates(color):
            return False

    return True

# Proposed grade: 0.43 / 1
# Test1: OK
# Test2: OK
# Test3: OK
# Test4: OK
# Test5: OK
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: Failed puzzle.validate_board([


@profile
def validate_board7(board: list) -> bool:
    """
    Validate the Sudoku board.
    """
    def check_duplicates(group):
        """
        Check for duplicates in a group (row, column, or color).
        """
        group = [x for x in group if x.isdigit()]
        return len(set(group)) == len(group)

    def extract_color_groups():
        """
        Extract tiles of the same color.
        """
        color_groups = []
        for i in range(5):
            color_groups.append([board[j][4 - i] for j in range(5 - i)] + [board[8 - j][i] for j in range(4 - i)])
        return color_groups

    for line in board:
        if not check_duplicates(line):
            return False

    for column in zip(*board):
        if not check_duplicates(column):
            return False

    for color_group in extract_color_groups():
        if not check_duplicates(color_group):
            return False

    return True

# Proposed grade: 0.38 / 1
# Test1: OK
# Test2: OK
# Test3: Failed puzzle.validate_board([
# Test4: OK
# Test5: Failed puzzle.validate_board([
# Test6: OK
# Test7: OK
# Test8: OK
# Test9: OK

if __name__ == "__main__":
    # Test cases
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
    validate_board1(board1)
    validate_board2(board1)
    validate_board3(board1)
    validate_board4(board1)
    validate_board5(board1)
    validate_board6(board1)
    validate_board7(board1)
    