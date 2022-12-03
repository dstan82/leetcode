from collections import Counter
import time

#Method 1 - no built-in functions 
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_occurences = {}
        word2_occurences = {}

        for letter in word1:
            if letter in word1_occurences:
                word1_occurences[letter] += 1
            else:
                word1_occurences[letter] = 1
        for letter in word2:
            if letter in word2_occurences:
                word2_occurences[letter] += 1
            else:
                word2_occurences[letter] = 1
        a = list(word1_occurences.values())
        b = list(word2_occurences.values())
        a.sort()
        b.sort()
   
        return set(word1) == set(word2) and a == b


obj = Solution()

#Method2 - using Counter
class Solution2:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = sorted(list(Counter(word1).values()))
        w2 = sorted(list(Counter(word2).values()))
        
        return set(word1) == set(word2) and w1 == w2

obj = Solution2()

print(obj.closeStrings("aabccc", "abbccc"))
print(obj.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))

a = 'aaabccdd'
b = '12345'

a = list(Counter(a).values())
a.sort()
print(a)
