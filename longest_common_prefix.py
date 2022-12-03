class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        curr_letter = ''
        l = 0
        prefix = ''
        list_count = 1
        while True:
            for i in range(len(strs)):
                if i+1 < len(strs) and strs[i][l] == strs[i+1][l]:
                    curr_letter = strs[i][l]
                    print(curr_letter)
                    list_count += 1
            if list_count == len(strs):
                prefix += curr_letter
            else:
                print (prefix)
            l += 1
        
        print(prefix)




obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])