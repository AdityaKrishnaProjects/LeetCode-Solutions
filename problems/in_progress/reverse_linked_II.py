class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    
    if left == right:
        return head

    

linkedlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(reverseBetween(linkedlist, 1, 5))