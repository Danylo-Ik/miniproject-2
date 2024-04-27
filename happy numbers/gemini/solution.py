def sieve_flavius(n: int) -> list:
    """
    This function takes an integer as user input and returns flavius numbers from its range
    >>> sieve_flavius(20)
    [1, 3, 7, 9, 13, 15]
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(-5)
    """
    if not isinstance(n, int) or n < 0:
        return None

    numbers_lst = [i for i in range(1, n + 1) if i % 2 != 0]
    k = 0
    result = []
    while k < len(numbers_lst):
        k += 1
        try:
            if numbers_lst[k] != "*":
                lucky = numbers_lst[k]
            else:
                while numbers_lst[k] == "*":
                    k += 1
                lucky = numbers_lst[k]
        except IndexError:
            break
        i = 0
        coef = 0
        while i < len(numbers_lst):
            if numbers_lst[i] != "*":
                coef += 1
                if coef % lucky == 0:
                    numbers_lst[i] = "*"
            i += 1
    result = [el for el in numbers_lst if el != "*"]
    return result