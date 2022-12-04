from math import floor

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        means = []
        for i in range(len(nums)):
            a = sum(nums[0:i+1])
            b = len(nums[0:i+1])
            c = floor(a/b)
            print(c)
        


        #return 

obj = Solution()
print(obj.minimumAverageDifference([2,5,3,9,5,3]))
