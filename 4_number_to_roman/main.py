"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def int_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "zero has no roman numeral"
        if number > 3999:
            return "number must not greater than 3999"

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman = ""
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman += symbols[i]
                number -= val[i]
            i += 1
        return roman

try:
    user_input = input("input = ").strip()
    number = int(user_input)
    solution = Solution()
    result = solution.int_to_roman(number)
    print(f"output = {result}")
except ValueError:
    print("Please enter a valid integer.")

