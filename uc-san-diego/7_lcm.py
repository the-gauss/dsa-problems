"""
5. Least Common Multiple Problem
Compute the least common multiple of two positive integers.
    Input: Two positive integers a and b.
    Output: The least common multiple of a and b.
Input format. Integers a and b (separated by a space)
Output format. LCM(a,b)
Sample:
    Input: 761457 614573
    Output: 467970912861
"""


def lcm(a, b):
    n = max(a, b)
    m = n
    while True:
        if m % a == 0 and m % b == 0:
            return m
        m += n


n = input()
n = n.split(' ')
a, b = int(n[0]), int(n[1])
print(lcm(a, b))
