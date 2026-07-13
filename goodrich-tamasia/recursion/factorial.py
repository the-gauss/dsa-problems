"""Factorial.

Here, each call to ``factorial(n)`` runs in O(1) time, and there are n+1 total
calls, so the runtime of the algorithm is O(n).

The factorial function can also be implemented using a loop as follows. It is
an incredibly inefficient algorithm, though.
"""


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_using_loop(n: int) -> int:
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact


if __name__ == "__main__":
    print(factorial(5))
    print(factorial_using_loop(5))
