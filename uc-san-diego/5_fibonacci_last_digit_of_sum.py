"""
Last Digit of the Sum of Fibonacci Numbers
Compute the last digit of F0 + F1 + ··· + Fn.
    Input: An integer n.
    Output: The last digit of F0 +F1 + ··· + Fn.

Input format: An integer n.
Output format: (F0 + F1 + ··· + Fn) mod 10

Sample 1.
    Input: 3
    Output: 4
Sample 2.
    Input: 100
    Output: 5
    F0 + ··· + F100 = 927372692193078999175.

Since the brute force approach for this problem is too slow, try to
come up with a formula for F0+F1+F2+···+Fn. Play with small values of n
to get an insight and use a solution for the previous problem afterward.
"""


# We here use the fact that the last digit of sum of two numbers is the same as the last digit of
# sum of their last digits
def fibonacci_last_digit_of_sum(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    sum_ = 1  # Initial sum (0 + 1)

    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
        sum_ = (sum_ + current) % 10

    return sum_


n = int(input())
print(fibonacci_last_digit_of_sum(n))
