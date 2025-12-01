class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Start is left and tail is node after right. Store next node from start as temp
# point start to tail, update tail to be start and start to be temp. Stitch tip 
# to final tail (last changed node). 
def reverseBetween(head, left, right):
    
    tail = head
    start = head

    for _ in range(right):
        tail = tail.next

    for _ in range(left-1):
        start = start.next

    for _ in range(right-left+1):
        temp = start.next

        start.next = tail
        tail = start

        start = temp

    tip = head

    if left == 1:
        head = tail
    for i in range(left-1):
        if i == left-2:
            tip.next = tail
        else:
            tip = tip.next

    return head

# linkedlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new = ListNode(1)

# print(reverseBetween(linkedlist, 1, 5))
print(reverseBetween(linkedlist2, 2, 4))
print(reverseBetween(new, 1, 1))