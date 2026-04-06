"""
2. Fibonacci Number Problem

Compute the n-th Fibonacci number.
    Input: An integer n.
    Output: n-th Fibonacci number
Sample 1.
    Input: 3
    Output: 2
Sample 2.
    Input: 10
    Output: 55
"""


# Bad Solution - Recursion
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    fibo_array = [0, 1]
    for i in range(2, n+1):
        a = fibo_array[i - 1] + fibo_array[i - 2]
        fibo_array.append(a)

    return fibo_array[n]


n = int(input())
print(fibonacci(n))
