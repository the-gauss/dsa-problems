"""Binary Search.

All the statements in ``binary_search()`` run in O(1) time, so runtime is
proportional to its number of calls. For data of size n, this is O(log n)
because the array is repeatedly divided in half until n/(2r) < 1, where r is
the number of calls.

This is a classic case of tail recursion. It uses O(log n) memory because
Python has no Tail Call Optimization. Converting it to an iterative algorithm
reduces the additional memory usage to O(1).
"""


def binary_search(target: int, data: list, low: int, high: int) -> bool:
    if low > high:
        return False
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    if target > data[mid]:
        return binary_search(target, data, mid + 1, high)
    return binary_search(target, data, low, mid - 1)


def binary_search_iterative(target: int, data: list, low: int, high: int) -> bool:
    while high >= low:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        if target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == "__main__":
    data = [1, 4, 6, 2, 23, 75, 12, 3, 90]
    print(binary_search(4, data, 0, len(data) - 1))
    print(binary_search(100, data, 0, len(data) - 1))
    print(binary_search_iterative(4, [1, 3, 5, 6], 0, 3))
