"""Reverse a Sequence in place using recursion in O(n) time."""


def reverse(S, start, stop):
    if start <= stop:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5]
    reverse(S, 0, 5)
    print(S)
