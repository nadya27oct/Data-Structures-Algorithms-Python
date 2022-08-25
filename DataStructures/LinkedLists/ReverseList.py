'''
Given a linked list 1->10->16->8, reverse the linked list 8->16->10->1

Initially current node = 10. Previous node = None.
    Then  current node = 16 & Previous node = 10
(null)  1 -> 10 -> 16 -> 8
prev  cur
      prev  cur
            prev  cur
                  prev  curr
                        prev

        1 <- 10 <- 16 <- 8
self.head = cur = 1,
next = cur.next = 10
cur.next = prev
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ReverseLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head

        while curr != None:
            next = curr.next # next =
            curr.next = prev
            prev = curr
            curr = next

        return prev

'''Time complexity = Big O(n); Memory complexity => Big O(1). We are using pointers but no data structures.
'''
