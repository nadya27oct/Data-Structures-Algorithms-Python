"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

1->2->3->4->5
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

1->2->3->4->5->6
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

We put each node in an array where key is count.
visited = {1->2->3->4->5, 2->3->4->5,  3->4->5,  4->5, 5->null}
length = len(visited) = 5 --> O(1) operation
middle = 5 // 2 = 2 => visited[middle] = 3->4->5 --> O(1) operation

1->2->3->4->5->6
0  1  2  3  4  5
if length = 6, middle = 3, so we want head of ll = 4->5->6->null

Approach 2:
3->null             middle=end=3
3 -> 2              middle=end=2
3->2->7             middle=2, end=7
3->2->7->4          middle=7, end=4
3->2->7->4->5       middle=7, end=5
3->2->7->4->5->1    middle=4, end=1
3->2->7->4->5->1->2    middle=4, end=2

1->2->3->4->5->6
m=e=1;
1st itertaion: m=2,e=3
2nd iteration: m=3,e=5;
3rd iteration: m=4,e=None; exit loop.

1->2->3->4->5
1st itertaion: m=2,e=3
2nd iteration: m=3,e=5; 5!=None but 5.next==None. Exit Loop. 
"""

class Node:

    def __init__(self,val=0):
        self.val = val
        self.next = None

    def middleNode(self,root):

        visited_nodes = []
        count = 0

        while root!=None:
            visited_nodes.append(root)
            count +=1
            root = root.next

        middle = len(visited_nodes) // 2
        return visited_nodes[middle]

    def middleNode_2(self,root):

        middle = root
        end = root

        while end != None and end.next != None:
            middle = middle.next #middle = 2,3,4
            end = end.next.next #end=3,5

        return middle

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six


ll = Node()
print(ll.middleNode(one))
print(ll.middleNode_2(one))
