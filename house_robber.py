'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count == 0:
            return 0
        elif count == 1:
            return nums[0]
        elif count == 2: 
            return max(nums[0], nums[1])
        
        memo = nums[:] # copy
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, count):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2]) 
        
        return memo[count-1]



obj = Solution()
func = obj.rob([31,4,6,18,6,1,3,8,1])
#21


print(func)