"""Deep Flattening.

Given a nested list of integers, where each element is either an integer or
another list (which can itself contain integers or lists), write a function to
return a single flat list containing all the integers in their original order.

Example Input: ``[1, [2, [3, 4], 5], 6, [7, 8]]``

Expected Output: ``[1, 2, 3, 4, 5, 6, 7, 8]``

The notebook contained this functional-recursion implementation twice; the
second copy was labelled "Recursive Generator: More memory efficient" but had
the same function body and usage example.
"""

from typing import Any, List


def flatten_recursive(nested_list: List[Any]) -> List[int]:
    """Flatten a nested list using recursion in O(N) total elements."""
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_recursive(element))
        else:
            flat_list.append(element)
    return flat_list


if __name__ == "__main__":
    data = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(flatten_recursive(data))
