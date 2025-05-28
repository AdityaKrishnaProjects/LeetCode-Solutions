# iterates through linked list
def deleteDuplicates(head):
    
    curr = head

    while curr is not None:
        temp = curr
        while temp and temp.val == curr.val:
            temp = temp.next
        curr.next = temp
        curr = temp

    return head