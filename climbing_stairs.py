class Solution:
    def climbStairs(self, n: int) -> int:
        number_of_2_steps = n//2
        even = n % 2
        if even == 0:
            combinations = 2
            for i in range(number_of_2_steps-1):
                combinations += n-(i+1)
        else:
            combinations = 1
            for i in range(number_of_2_steps):
                combinations += n-(i+1)

        return combinations

obj = Solution()

print(obj.climbStairs(1))
print(obj.climbStairs(2))
print(obj.climbStairs(3))
print(obj.climbStairs(5))
print(obj.climbStairs(6))