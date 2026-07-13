import sys
import random

def max_pairwise_product(n, a):
    first = max(a)
    a.remove(first)
    second = max(a)

    return first*second

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))

    # passed = stress_test(n, a)
    max_product = max_pairwise_product(n, a)
    print(max_product)

main()

#BETTER SOLUTION
# def max_pairwise_product(a):
#     # Initialize the two largest numbers
#     first_max = second_max = -sys.maxsize
#
#     for number in a:
#         if number > first_max:
#             # Update both first and second max
#             second_max = first_max
#             first_max = number
#         elif number > second_max:
#             # Update only second max
#             second_max = number
#
#     return first_max * second_max
#
# def main():
#     n = int(input())
#     a = list(map(int, input().split(' ')))
#
#     max_product = max_pairwise_product(a)
#     print(max_product)
#
# main()
