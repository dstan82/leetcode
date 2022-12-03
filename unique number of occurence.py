class Solution:
    def __init__ (self):
        self.occurences = {}
    def uniqueOccurrences(self, arr: list[int]) -> bool:
                
        for num in arr:
            if num in self.occurences:
                self.occurences[num] += 1
            else:
                self.occurences[num] = 1
        return (len(self.occurences.values()) == len(set(self.occurences.values())))



obj = Solution()
print(obj.uniqueOccurrences([1,1,2,2,1,1,3,3]))
            