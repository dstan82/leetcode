class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        i = 0
        while i+1 < l:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
            l = len(nums)
        return len(nums)

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
