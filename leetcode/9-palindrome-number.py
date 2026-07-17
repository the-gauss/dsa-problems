"""9. Palidrome Number

Refer to https://leetcode.com/problems/palindrome-number/ for the problem
statement.

This improves the previous solution because it does not need O(n) string
space: it manipulates the integer itself.

Time Complexity: O(log_10 x), proportional to the number of digits in x.
Space Complexity: O(1).
"""


def is_palindrome_int(x: int) -> bool:
    if x < 0:       # Negative numbers can't be palindromes
        return False
    original = x
    reverse = 0
    while x / 10 != 0:
        last = x % 10
        x = x // 10
        reverse = last + reverse * 10
    return reverse == original


if __name__ == "__main__":
    tests = [121, -121, 10001, 10, 0, 200000000000000002]
    for t in tests:
        print(t, is_palindrome_int(t))

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

"""9. Palidrome Number — Solution 3: The Optimal Solution.

Refer to https://leetcode.com/problems/palindrome-number/ for the problem
statement.

A palindrome is mirrored at its center, so reverse only the second half and
compare it to the first. This also reduces the risk of integer overflow in
statically typed languages such as Java and C++ (though it is not a major
problem in Python). Time and space complexity are the same as Solution 2.
"""


def is_palindrome(x: int) -> bool:
    # Fast fail: All negative numbers are not palindromes.
    # Numbers ending in 0 (but not 0 itself) cannot be palindromes.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed = 0

    # Only reverse until the reversed half is at least the remaining half.
    while x > reversed:
        reversed = (reversed * 10) + x % 10
        x //= 10

    # For even digit lengths, x == reverted.
    # For odd digit lengths, drop the middle digit using reverted // 10.
    return x == reversed or x == reversed // 10


if __name__ == "__main__":
    tests = [121, -121, 10001, 10, 0, 200000000000000002]
    for t in tests:
        print(t, is_palindrome(t))
