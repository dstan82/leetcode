class node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class linked_list:
    def __init__(self) -> None:
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total
    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
    def get(self,index):
        if index >= self.length():
            print('Error GET index out of range')
            return None
        cur_idx = 0
        current_node = self.head.next
        while True:
            if cur_idx == index: 
                return current_node.data
            cur_idx += 1
            current_node = current_node.next
        
    def pop(self, index):
        if index >= self.length():
            print('Error POP index out of range')
            return None
        cur_idx = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if cur_idx == index:
                last_node.next = current_node.next
                return None
            cur_idx += 1


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.display()
print(f'list length: {my_list.length()}')
print(my_list.get(6))
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)

print(my_list.head.data)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        list_length = 1
        cur = head
        while cur:
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


