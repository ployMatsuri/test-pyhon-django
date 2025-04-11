"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        i=0
        max_index = 0

        for i in range(len(numbers)):
            if numbers[i]<0:
                return "number can not be negative"
            
            if numbers[i] >= numbers[max_index]:
                max_index=i
                
        return max_index
    
try:
    user_input = input("input = ")
    
    if not (user_input.startswith('[') and user_input.endswith(']')):
        raise ValueError("Invalid format")

    content = user_input.strip('[]').strip()
    
    if content == "":
        numbers = []
    else:
        numbers = list(map(int, content.split(',')))

    solution = Solution()
    result = solution.find_max_index(numbers)
    print(f"output = {result}")
    
except ValueError:
    print("Please enter a valid list of integers.") 
        
