"""Power.

The following algorithms calculate x^n for integers x and n. The first,
``power_bad()``, although not too bad, runs in O(n) time.

The first algorithm has O(n) runtime and memory because O(n) records are held
simultaneously at recursion depth O(n). The second runs in O(log n) time and
memory.
"""


def power_bad(x: int, n: int) -> int:
    if n < 1:
        return 1
    return x * power_bad(x, n - 1)


def power(x: int, n: int, call_n=0) -> int:
    if n < 1:
        return 1
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


if __name__ == "__main__":
    print(power(4, 4))
