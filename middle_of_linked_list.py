class node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class linked_list:
    def __init__(self,mandatory_first_element) -> None:
        self.head = node(mandatory_first_element)
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)
    def get(self,index):
        if index >= self.length():
            print('Error GET index out of range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_idx == index: 
                return cur_node.data
            cur_idx += 1
            cur_node = cur_node.next
        
    def pop(self, index):
        if index >= self.length():
            print('Error POP index out of range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_idx == index:
                if cur_idx == 0:
                    self.head = self.head.next
                    print('head poped, next elem is now head')
                    return None
                last_node.next = cur_node.next
                print('elem poped')
                return None
            last_node = cur_node
            cur_node = cur_node.next
            cur_idx += 1
                
        


my_list = linked_list(0)
print(my_list.head.data)
my_list.append(1)
next = my_list.head.next
print(next.data)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list.length())
my_list.display()
print(my_list.get(0))
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.display()
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


