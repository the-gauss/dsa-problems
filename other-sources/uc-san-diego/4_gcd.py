"""
4. Greatest Common Divisor Problem
Compute the greatest common divisor of two positive integers.
    Input: Two positive integers a and b.
    Output: The greatest common divisor of a and b.
Input format: Integers a and b (separated by a space).
Output format: GCD(a,b)
Sample:
    Input: 28851538 1183019
    Output: 17657

"""

# Bad Solution - Too Slow
# def gcd(a,b):
#     n = min(a, b)
#     for i in range(n+1, 0, -1):
#         if a%i == 0 and b%i==0:
#             return i

def gcd(a, b):
    """
    Uses the fact that GCD of two numbers a and b is the same as GCD of a%b and b
    """
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    n = a % b
    a = b
    b = n
    return gcd(a, b)


inp = input().split(' ')
a, b = int(inp[0]), int(inp[1])
print(gcd(a, b))
