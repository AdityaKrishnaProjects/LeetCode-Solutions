
# pretty trash solution
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Initialize the pointers
    if list1.val <= list2.val:
        curr_head = list1
        pot_head = list2
    else:
        curr_head = list2
        pot_head = list1

    # Keep track of the starting node
    return_head = curr_head

    # Iterate and merge
    while curr_head.next:
        if pot_head is None:
            break

        if pot_head.val <= curr_head.next.val:
            # Insert pot_head between curr_head and curr_head.next
            temp = curr_head.next
            curr_head.next = pot_head
            pot_head = pot_head.next
            curr_head.next.next = temp

        curr_head = curr_head.next

    # If pot_head still has elements, attach it at the end
    if pot_head:
        curr_head.next = pot_head

    return return_head