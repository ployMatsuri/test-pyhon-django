"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        count = 0
        i=5

        while number // i > 0:
            count += number//i
            print(number//i)
            print(count)
            i*=5
        return count
    
try:
    number = int(input("input = "))
    solution = Solution()
    result = solution.find_tailing_zeroes(number)
    print(f"output = {result}")
except ValueError:
    print("Please enter a valid integer.")
