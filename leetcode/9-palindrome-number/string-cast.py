"""9. Palidrome Number — Solution 1: The String Cast.

Refer to https://leetcode.com/problems/palindrome-number/ for the problem
statement.

The Good: It is highly Pythonic, concise, and correctly handles negative
numbers because the minus sign is preserved in the string reversal ("-121"
becomes "121-", which correctly evaluates to False).

The Bad: It is an entry-level shortcut. In an algorithmic interview, or a
highly constrained environment, this approach is a failure. You allocate extra
memory to create two string objects: O(n) space, where n is the number of
digits. The core intent is to manipulate integers mathematically, not use
Python string slicing.
"""


def is_palindrome_str(x: int) -> bool:
    return str(x)[::-1] == str(x)


if __name__ == "__main__":
    tests = [121, -121, 10001, 10, 0, 200000000000000002]
    for t in tests:
        print(t, is_palindrome_str(t))
