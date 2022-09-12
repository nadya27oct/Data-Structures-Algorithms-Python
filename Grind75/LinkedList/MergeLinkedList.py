"""
Given two sorted linked list, merge them to one.
list1 -> 1->2->4-> NULL
list2 -> 1->3->5-> NULL
head1 -> 1->1->2->3->4->5->NULL

Compare 1st values from both lists. This is the lowest.
1 <= 1: head1 = list1; list1 is at 2. list2 is at 1; head1: 1
2 >= 1: head1 = list2; list1 is at 2. list2 is at 3; head1: 1->1
2 <= 3: head1 = list1; list1 is at 4. list2 is at 3; head1: 1->1->2
4 >= 3; head1 = list2; list1 is at 4. list2 is at 5; head1: 1->1->2->3
4 <= 5; head1 = list1; list1 is over. list2 is at 5; head1: 1->1->2->3->4

Add the remaining nodes to head1.

Dummy Node - If head node is null then point head to new node. Otherwise, we use different code.
Dummy node accounts for that special case by avoiding that special case.
Front is not a node, it is reference to a node, starting point.
Insert extra node in beginning that has its data null.
Dummy node sits in between front reference and the actual data node.
dummy = Node() => {val:0, next = None}
In this example, dummy will output 0->1->1->2->3->4->5->NULL
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self,list1,list2):

        dummy = Node() # list={val:1,next:None}

        curr = dummy Current needs

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 == None:
            curr.next = list2

        if list2 == None:
            curr.next = list1

        return dummy.next
