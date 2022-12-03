class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexes = {}
        i = 0
        last_index = 0
        distance = 0
        for letter in keyboard:
            indexes[letter] = i
            i += 1
        print(indexes)
        print (word)
        for letter in word:
            distance += abs(indexes[letter] - last_index)
            last_index = indexes[letter]


        return distance


obj = Solution()
print(obj.calculateTime("abcdefghijklmnopqrstuvwxyz", 'cba'))