"""13. Roman to Integer.

Refer to https://leetcode.com/problems/roman-to-integer/ for the problem
statement.
"""


def roman_to_int(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total


if __name__ == "__main__":
    print(roman_to_int("III"))      # 3
    print(roman_to_int("IV"))       # 4
    print(roman_to_int("IX"))       # 9
    print(roman_to_int("LVIII"))    # 58
    print(roman_to_int("MCMXCIV"))  # 1994
