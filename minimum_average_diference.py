from math import floor

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        diff = {}
        for i in range(len(nums)):
            a = sum(nums[0:i+1])
            b = len(nums[0:i+1])
            p1 = floor(a/b)
            c = sum(nums[i+1:])
            d = len(nums[i+1:])
            p2 = floor(c/d) if d != 0 else 0
            diff[i] = abs(p2-p1)
        return(min(diff, key=diff.get))


obj = Solution()
print(obj.minimumAverageDifference([2,5,3,9,5,3]))
