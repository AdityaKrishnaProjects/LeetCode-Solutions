# O(1) space and O(m+n) time. Could also determine the longer list and then 
# standardize the starting position of each list to reach the end of the list 
# at the same time. If they ever intersect they will reach the intersection node 
# at the same time.
def getIntersectionNode(headA, headB):
    curr = headA

    while curr:
        curr.val *= -1
        curr = curr.next

    curr2 = headB

    while curr2:
        if curr2.val < 0:
            while headA:
                headA.val *= -1
                headA = headA.next

            return curr2

        curr2 = curr2.next
        
    while headA:
        headA.val *= -1
        headA = headA.next

    return None