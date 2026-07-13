"""9. Palidrome Number — Solution 2: Using Integer Manipulation.

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
