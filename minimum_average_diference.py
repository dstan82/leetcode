from math import floor
import time

'''
#Method1
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        diff = {}
        index = 0
        sum1 = 0
        total_length = len(nums)
        total_sum = sum(nums)
        for num in nums:
            sum1 += num
            average1 = floor(sum1/(index+1))
            sum2 = total_sum - sum1
            index += 1
            average2 = floor(sum2 / (total_length-index) if total_length-index != 0 else 0)
            diff[index-1] = abs(average2-average1)
        return min(diff, key=diff.get)

#Method2
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        index = 0
        sum1 = 0
        total_length = len(nums)
        total_sum = sum(nums)
        max_dif = max(nums)
        for num in nums:
            sum1 += num
            average1 = floor(sum1/(index+1))
            sum2 = total_sum - sum1
            index += 1
            average2 = floor(sum2 / (total_length-index) if total_length-index != 0 else 0)
            if max_dif > abs(average2-average1):
                max_dif = abs(average2-average1)
                result = index - 1
        return result
'''

#Method3
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        index = 0
        sum1 = 0
        total_sum = sum(nums)
        total_length = len(nums)
        diff = {}
        for num in nums:
            sum1 += num
            average1 = sum1//(index+1)
            sum2 = total_sum - sum1
            index += 1
            average2 = sum2 // (total_length-index) if total_length-index != 0 else 0
            diff[index-1] = abs(average2-average1)
        return min(diff, key=diff.get)


obj = Solution()
list0 = [2,5,3,9,5,3]

a = time.time()
print(obj.minimumAverageDifference(list0))
b = time.time()

print((b-a)*1000)
