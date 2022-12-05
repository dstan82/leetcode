class node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class linked_list:
    def __init__(self) -> None:
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        list_length = 1
        cur = head
        while cur.next != None :
            list_length += 1
            cur = cur.next
        mid_node = list_length // 2
        cur = head
        for i in range(mid_node):
            cur = cur.next
        return cur

linke_list = Solution()
result = linke_list.middleNode(my_list.head.next)
print(result.data)


