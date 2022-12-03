'''
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('[]','').replace('{}','')
            if l == len(s):
                return False
        return True

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')':'(', '}':'{', ']':'['}

        for p in s:
            print(f'{p} iteration strt')
            if p in lookup.values():
                print(f'1 {stack}')
                stack.append(p)
                print(f'2 {stack}')
            elif stack and lookup[p] == stack[-1]:
                print(f'3 {stack}')
                stack.pop()
                print(f'4 {stack}')
            else:
                return False
            print(f'{p} iteration end')

        return stack == []




obj = Solution()
print(obj.isValid("({())"))
#print(obj.isValid("{[]}"))
#print(obj.isValid("(){}}{"))
