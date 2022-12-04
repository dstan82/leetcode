from math import floor

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        means = []
        for i in range(len(nums)):
            a = sum(nums[0:i+1])
            b = len(nums[0:i+1])
            p1 = floor(a/b)
            c = sum(nums[i+1:])
     #       print(c)
            d = len(nums[i+1:])
      #      print(d)
            p2 = floor(c/d) if d != 0 else 0
            means.append(p2)
        print(means)


        #return 

obj = Solution()
print(obj.minimumAverageDifference([2,5,3,9,5,3]))
