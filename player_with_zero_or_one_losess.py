class Solution:
    def __init__(self) -> None:
        self.summary = {}
        self.winners = []
        self.loosers = []

    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        
        for match in matches:
            self.summary[match[0]] = 0
            self.summary[match[1]] = 0
      
        for match in matches:
            self.summary[match[1]] += 1
        
        for player in self.summary:
            if self.summary[player] == 0:
                self.winners.append(player)
            elif self.summary[player] == 1:
                self.loosers.append(player)
#        self.winners.sort()
 #       self.loosers.sort()
        return [sorted(self.winners), sorted(self.loosers)]






obj = Solution()
print(obj.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

'''
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8]
'''