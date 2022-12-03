class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digit_index = []
        index = 0
        result = []
        for i in number:
            if int(i) == int(digit):
                digit_index.append(index)
            index += 1
        num = [int(x) for x in str(number)]
        for i in digit_index:
            num = [int(x) for x in str(number)]
            num.pop(i)
            result.append(int("".join(map(str, num))))
        return str(max(result))
        


obj = Solution()
print(obj.removeDigit("123", "3"))