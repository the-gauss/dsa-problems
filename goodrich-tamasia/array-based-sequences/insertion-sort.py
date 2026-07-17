"""Sorting a Sequence with insertion sort."""


def insertion_sort(A):
    for k in range(len(A)):
        cur = A[k]
        j = k
        while j > 0 and cur < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur
    return A


if __name__ == "__main__":
    A = [3, 5, 7, 4, 2, 9, 5]
    print(insertion_sort(A))
