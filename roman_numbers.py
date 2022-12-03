class Solution:
    def romanToInt(self, s: str) -> int:
        arab_nr = 0
        i = 0
        while i < len(s):
            if len(s)-1 > i and s[i] == 'I' and s[i+1] == 'V':
                    arab_nr += 4
                    i += 2
            elif len(s)-1 > i and s[i] == 'I' and s[i+1] == 'X':
                    arab_nr += 9
                    i += 2
            elif len(s)-1 > i and s[i] == 'X' and s[i+1] == 'L':
                    arab_nr += 40
                    i += 2
            elif len(s)-1 > i and s[i] == 'X' and s[i+1] == 'C':
                    arab_nr += 90
                    i += 2
            elif len(s)-1 > i and s[i] == 'C' and s[i+1] == 'D':
                    arab_nr += 400
                    i += 2
            elif len(s)-1 > i and s[i] == 'C' and s[i+1] == 'M':
                    arab_nr += 900
                    i += 2
            elif s[i] == 'I':
                arab_nr += 1
                i += 1
            elif s[i] == 'V':
                arab_nr += 5
                i += 1
            elif s[i] == 'X':
                arab_nr += 10
                i += 1
            elif s[i] == 'L':
                arab_nr += 50
                i += 1
            elif s[i] == 'C':
                arab_nr += 100
                i += 1
            elif s[i] == 'D':
                arab_nr += 500
                i += 1
            elif s[i] == 'M':
                arab_nr += 1000
                i += 1
        print(arab_nr)
        return arab_nr

solution = Solution()
solution.romanToInt('III')
solution.romanToInt('LVIII')
solution.romanToInt('MCMXCIV')
print(solution.romanToInt.__annotations__)