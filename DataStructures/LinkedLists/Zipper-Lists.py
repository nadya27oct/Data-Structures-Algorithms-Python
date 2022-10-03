"""
Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
The function should zipper the two lists together into single linked list by alternating nodes.
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
The function should return the head of the zippered linked list.

list1: s -> t
list2: 1 -> 2 -> 3 -> 4
zipper_lists(s, one) = s -> 1 -> t -> 2 -> 3 -> 4

Since we do not know list size, we cannot use two pointer sum.
Let count = 0, increment count at each traversal.
If count is odd, use list2 nodes to attach and if count is even use list1.
At start, current1 = list1 each traversal, update current.

Tail - Reference to add new nodes to our current output.

count = 0, cur1 = head1.next = t, cur2 = 1
tail = s
tail.next = cur2 = 1: s->1, count = 1, cur2=2

s->1->t->
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

s = Node("s")
t = Node("t")
s.next = t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four

def zipper_lists(head1,head2):

    count=0
    tail = head1  # tail = head1 = s
    current1 = head1.next # move current1 to next in list2: cur1=t
    current2 = head2 # cur2=1

    while current1 != None and current2 != None:
        if count % 2 ==0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        count +=1
        tail = tail.next

    if current1==None:
        tail.next = current2

    if current2==None:
        tail.next = current1

    final = []
    cur = head1
    while cur != None:
        final.append(cur.val)
        cur = cur.next

    return final

zipper_lists(s,one)

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z

# a -> x -> b -> y -> c -> z

"""
Recursion for zipper lists:
Base cases:
1. Stop recursion if head1 is null and head2 is null. Return null.
2. If head1 is null, return head2. If head2 is null, return head1. For leftover nodes, just append remaining nodes
to head.

Save pointers before overriding them.
In head1, s->t, so next1 = t. In head2, 1->2->3->4, so next2=2.
next1 = head1.next
next2 = head2.next
Then head1 should recursively point to head2, ex: s->1
zipper list will return head1 of remaining linked list. so we call recursive_zipper_list function.

head1: a  ->  b -> c
       h1    n1
head2: x  ->  y -> z
       h2    n2
h1->h2: a->x->zipper_list(b,y)

head1: b -> c
       h1    n1
head2: y -> z
       h2    n2
h1->h2: b->y->zipper_list(c,z)
a->x->b->y->zipper_list(c,z)

head1: b -> c
       h1    n1
head2: y -> z
       h2    n2
h1->h2: c->z
a->x->b->y->c->z
"""

def recursive_zipper_list(head1,head2):

    if head1 == None:
        return head2

    if head2 == None:
        return head1

    next1 = head1.next # In list1: s->t, We don't want to lose t, when we point s->1 in next step. so next1 = t
    next2 = head2.next # list2: 1->2->3->4; next2=2
    head1.next = head2 # s->1,
    head2.next = recursive_zipper_list(next1,next2)

    return head1

def display_ll(head):

    arr = []
    current = head
    while current != None:
        arr.append(current.val)
        current = current.next

    return arr

final = recursive_zipper_list(a,x)
print(display_ll(final))
