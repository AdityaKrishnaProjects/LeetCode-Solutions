class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Pretty decent solution
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    while head:
        if head.val == "seen":
            return True
        head.val = "seen"
        head = head.next
    return False

i = ListNode(3)
j = ListNode(2)
k = ListNode(0)
l = ListNode(-4)

i.next = j
j.next = k
k.next = l
l.next = j

head = i

print(hasCycle(head))

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d

head2 = a

print(hasCycle(head2))