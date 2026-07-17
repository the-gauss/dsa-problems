"""
66. Plus One
https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150

The following solution runs in O(n) time and uses O(1) memory except the +[1]. This is
the standard solution, and uses the same addition algorithm taught in elementary school.
"""
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i]!=9:
            digits[i]+=1
            return digits

        digits[i]=0

    return [1] + digits
