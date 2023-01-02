class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern = list(pattern)
        pairs = {}
        if len(s) != len(pattern): return False
        while pattern:
            current_pattern = pattern.pop(0)
            current_s = s.pop(0)
            if current_s in pairs.values():
                if [k for k, v in pairs.items() if v == current_s][0] != current_pattern:
                    return False
            elif current_pattern in pairs:
                if pairs[current_pattern] != current_s:
                    return False
            else:
                pairs[current_pattern] = current_s
        return True
    
obj = Solution()

print(obj.wordPattern('abbac', 'cat fish fish cat cat'))


