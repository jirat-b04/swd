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

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"

        if number == 0:
            return "ศูนย์"

        digits = [
            "", "หนึ่ง", "สอง", "สาม", "สี่",
            "ห้า", "หก", "เจ็ด", "แปด", "เก้า"
        ]

        positions = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน"]

        def convert(n: int) -> str:
            result = ""
            num_str = str(n)
            length = len(num_str)

            for i, ch in enumerate(num_str):
                digit = int(ch)

                if digit == 0:
                    continue

                pos = length - i - 1

                if pos == 0:
                    if digit == 1 and length > 1:
                        result += "เอ็ด"
                    else:
                        result += digits[digit]

                elif pos == 1:
                    if digit == 1:
                        result += "สิบ"
                    elif digit == 2:
                        result += "ยี่สิบ"
                    else:
                        result += digits[digit] + "สิบ"

                else:
                    result += digits[digit] + positions[pos]

            return result

        if number < 1_000_000:
            return convert(number)

        million = number // 1_000_000
        remainder = number % 1_000_000

        result = convert(million) + "ล้าน"

        if remainder:
            result += convert(remainder)

        return result
    
sol = Solution()
print(sol.number_to_thai(101))
print(sol.number_to_thai(-1))
