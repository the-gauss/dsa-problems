"""Fibonacci.

Returning the nth Fibonacci number.

``bad_fibonacci`` is a terrible algorithm: it runs in O(2^n) time. There are
two recursive calls in each call, each growing exponentially in the input size
at every level. Let c_n represent the number of calls: c_0 = 1, c_1 = 1,
c_2 = 1 + c_0 + c_1 = 3, c_3 = 1 + c_1 + c_2 = 5,
c_4 = 1 + c_2 + c_3 = 9, and c_7 = 1 + c_5 + c_6 = 41.

Instead, return a pair of Fibonacci numbers so a number calculated at the
previous recursion level is passed up at the next level, avoiding additional
calculation. The following algorithm runs in O(n).
"""


def bad_fibonacci(n):
    if n <= 1:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


def fibonacci(n):
    if n <= 1:
        return (0, n)  # Returns (0, 1) on n = 1, the first pair.
    a, b = fibonacci(n - 1)
    return (b, a + b)


if __name__ == "__main__":
    print(fibonacci(5))  # Fourth and fifth Fibonacci numbers.
