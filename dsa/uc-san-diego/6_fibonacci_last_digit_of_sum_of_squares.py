"""
Last Digit of the Sum of Squares of Fibonacci Numbers Problem
Sample 1.
Input:
7
Output:
3

Since the brute force search algorithm for this problem is too slow, we shall use the fact that the sum of squares upto
nth fibonacci number = the are of the rectange whose sides are F[n] and F[n+1],
for example, the sum of squares of first 5 (4rth index) fibonacci numbers = F[4] x F[5] = 3x5
"""

def fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    return current

def last_digit_of_sum_of_squares(n):
    if n < 0:
        return 0
    # Get the last digit of the n-th and (n+1)-th Fibonacci numbers
    nth_fibo = fibonacci(n) % 10
    nth_plus_one_fibo = fibonacci(n+1) % 10

    # The last digit of the product of these two numbers
    return (nth_fibo * nth_plus_one_fibo) % 10


n = int(input())
print(last_digit_of_sum_of_squares(n))