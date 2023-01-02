import math

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        # combinations of dominoes
        domino_comb = math.factorial(n)//math.factorial(n-1)
        if (2*n)%3 == 0:
            tromino_nr = (2*n)//3
            tromino_comb = math.factorial(tromino_nr)//math.factorial(tromino_nr-1)
        else:
            tromino_nr = (2*n)//3
            tromino_comb = math.factorial(tromino_nr)//math.factorial(tromino_nr-1)
        return domino_comb+tromino_comb
obj = Solution()

print(obj.numTilings(4))