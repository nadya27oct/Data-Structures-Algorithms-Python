'''
Given a linked list 1->10->16->8, reverse the linked list.
 1 <- 10 <- 16 <- 8.

Reverse each pointer.
Initially current node = 10. Previous node = None.
    Then  current node = 16 & Previous node = 10
(null)  1 -> 10 -> 16 -> 8
prev  cur
      prev  cur
            prev  cur
                  prev  curr
                        prev

        1 <- 10 <- 16 <- 8
Currently, Head points to 1,
Head -> 1, Next -> 10.
Reversing: Prev -> Null, Cur Head -> 10.


Head -> 8
next = cur.next = 10
cur.next = prev
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add_to_start(self,val):

        new_node = node(val)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head

        ll = []
        while current != None:
            ll.append(current.data)
            current = current.next

        return ll

    def reverse(self):
        prev = None
        curr = self.head

        while curr != None:
            next = curr.next # next is 10
            curr.next = prev # now 10 needs to point to 1.
            prev = curr # 1 is previous.
            curr = next # 10 is now current.
            print('prev',prev.data)
            if curr != None:
                print('curr',curr.data)

        self.head = prev

        return

ll = linkedlist()
ll.add_to_start(3)
ll.add_to_start(2)
ll.add_to_start(1)
print(ll.display())

ll.reverse()
print(ll.display())

'''
Time complexity = Big O(n); Memory complexity => Big O(1). We are using pointers but no data structures.
head
'''
