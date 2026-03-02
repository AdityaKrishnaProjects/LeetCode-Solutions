# linked lists
def removeElements(head, val):
    dummy = ListNode(0, head)

    curr = dummy

    while curr:
        while curr.next and (curr.next.val == val):
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next