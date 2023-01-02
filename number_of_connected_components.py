#
test_1 = [[0,1],[1,2],[3,4]]
test_2 = [[0,1],[1,2],[2,3],[3,4]]
test_3 = [[0,1],[1,2],[0,2],[3,4]]
test_4 = [[2,3],[1,2],[1,3]]


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        elements = {}
        elem_no = 1
        item_already_existed = False
        while edges:
            item_already_existed = False
            node = edges[0]
            for elem in elements:
                if node[0] in elements[elem] or node[1] in elements[elem]:
                    elements[elem].extend([node[0], node[1]])
                    item_already_existed = True
            if item_already_existed is False: 
                elements[elem_no]= [node[0], node[1]]
                elem_no += 1
            edges.pop(0)
        return len(elements)

n = 5
obj = Solution()
#print(obj.countComponents(n,test_1))
#print(obj.countComponents(n,test_2))
#print(obj.countComponents(n,test_3))
print(obj.countComponents(n,test_4))