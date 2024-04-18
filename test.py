"""
Find factorials and fibonacci numbers
both recursively and iteratively
"""
import time

@profile
def factorial_recursive(n: int, depth=0) -> int:
    """
    find factorial of n recursively
    >>> factorial_recursive(10)
    3628800
    >>> factorial_recursive(-3)
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    return factorial_recursive(n - 1, depth + 1) * n


def factorial_iterative(n: int) -> int:
    """
    find factorial of n iteratively
    >>> factorial_iterative(10)
    3628800
    >>> factorial_iterative(-3)
    """
    if n < 0:
        return None
    factorial = n
    while n != 1:
        factorial *= (n - 1)
        n -= 1
    return factorial


def fibonacci_recursive(n: int, depth=0) -> int:
    """
    find the n-th member of the fibonacci sequence recursively
    >>> fibonacci_recursive(5)
    8
    >>> fibonacci_recursive(-3)
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1, depth + 1) + fibonacci_recursive(n - 2, depth + 1)


def fibonacci_iterative(n: int) -> int:
    """
    find the n-th member of the fibonacci sequence iteratively
    >>> fibonacci_recursive(5)
    8
    >>> fibonacci_recursive(-3)
    """
    if n < 0:
        return None
    fib_seq = [1, 1]
    counter = 1
    while counter != n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        counter += 1
    return fib_seq[-1]

if __name__ == "__main__":
    factorial_recursive(100)