# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        r1 = l1[::-1]
        r2 = l2[::-1]
        i1 = ""
        i2 = ""
        for elem in r1:
            i1 += str(elem)
        for elem in r2:
            i2 += str(elem)
        result = str(int(i1)+int(i2))[::-1]
        result_list = []
        for elem in result:
            result_list.append(int(elem))
        return result_list



test_obj = Solution()
print(test_obj.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))