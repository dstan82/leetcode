class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half = s[0:len(s)//2]
        second_half = s[len(s)//2:]
        first_counter = 0
        second_counter = 0
        vowels = set('aeiou')
        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                first_counter += 1
            if s[len(s)//2+i].lower() in vowels:
                second_counter += 1
        return first_counter == second_counter
obj = Solution()
print(obj.halvesAreAlike('Baooak'))