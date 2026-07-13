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
