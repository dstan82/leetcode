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

my_list.append(0)
my_list.append(1)
my_list.append(2)
'''
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
'''

my_list.display()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        current_node = head.head.next
        list_length = 1
        if current_node == None or current_node.next == None or current_node.next.next == None:
            return head
        else:
            keep_even_head = current_node.next

        while current_node.next.next != None:
            list_length += 1
            next_node = current_node.next
            current_node.next = next_node.next
            current_node = next_node

        if list_length %2 == 0:
            current_node.next.next = keep_even_head
            current_node.next = None
        else:
            print(current_node.next.data)
            current_node.next = None
            print(current_node.data)
            current_node.next = keep_even_head
            
        return head


obj = Solution()
result = obj.oddEvenList(my_list)
result.display()