"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def number_to_thai_text(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"
        if number > 10_000_000:
            return "number must not greater than 10,000,000"
        
        digit_text = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        position_text = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        def convert_6digit(n):
            result = ""
            str_n = str(n)
            length = len(str_n)
            for i in range(length):
                digit = int(str_n[i])
                pos = length - i - 1
                if digit == 0:
                    continue
                if pos == 1 and digit == 1:
                    result += "สิบ"
                elif pos == 1 and digit == 2:
                    result += "ยี่สิบ"
                elif pos == 1:
                    result += digit_text[digit] + "สิบ"
                elif pos == 0 and digit == 1 and length > 1:
                    result += "เอ็ด"
                else:
                    result += digit_text[digit] + position_text[pos]
            return result

        text = ""
        if number >= 1_000_000:
            millions = number // 1_000_000
            text += convert_6digit(millions) + "ล้าน"
            number %= 1_000_000

        text += convert_6digit(number)
        return text


try:
    user_input = input("input = ")
    number = int(user_input)
    solution = Solution()
    result = solution.number_to_thai_text(number)
    print(f"output = {result}")
except ValueError:
    print("Please enter a valid integer.")

