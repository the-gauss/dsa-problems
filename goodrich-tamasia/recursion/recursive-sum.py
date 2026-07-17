"""Recursive Sum of an Array.

This computes the sum of the first n numbers of the sequence S (an array-like
object) in O(n) time.

We can improve it further by using binary recursion. Split the list in half
and add each half recursively. This runs in the same O(n) time but uses only
O(log n) additional memory instead of O(n) in the previous implementation.
"""


def recursive_sum(S, n):
    if n < 1:
        return 0
    return recursive_sum(S, n - 1) + S[n - 1]


def binary_sum(S, start, stop):
    """Sum a range; start and stop allow selecting a specific range."""
    if stop <= start:
        return 0
    if stop - 1 == start:
        return S[start]
    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    print(recursive_sum(values, 7))
    print(binary_sum(values, 0, 7))
