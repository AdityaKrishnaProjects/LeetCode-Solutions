# The following is solved horribly since I initially solved it just using lists 
# and not linked lists. What came after was a hamfisted linked list 
# transformation of the solution that worked on lists 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def linked_list_to_list(head):
            result = []
            current = head
            while current:
                result.append(current.val)  # Add current node's value to the list
                current = current.next  # Move to the next node
            return result

        def list_to_linked_list(lst):
            if not lst:
                return None  # Return None if the input list is empty
            head = ListNode(lst[0])  # Create the head of the linked list
            current = head
            for val in lst[1:]:
                current.next = ListNode(val)  # Create the next node and link it
                current = current.next  # Move to the next node
            return head

        l1 = linked_list_to_list(l1)
        l2 = linked_list_to_list(l2)

        l1_num, l2_num = 0, 0
        i,j = 10**(len(l1)-1), 10**(len(l2)-1)

        while l1:
            # print("multiplier for l1 is", i) 
            l1_num = l1_num + (l1.pop()*i)
            # print("current value of l1 is", l1_num)
            i = i/10

        while l2: 
            # print("multiplier  for l2 is", j)
            l2_num = l2_num + (l2.pop()*j)
            # print("current value of l2 is", l2_num)
            j = j/10

        total = list(str(int(l1_num + l2_num)))
        reversed_list = []
        
        while total:
            reversed_list.append(int(total.pop()))

        return list_to_linked_list(reversed_list)


print("linked list is", addTwoNumbers([8,9,9], [4,5,6]), "\n \n")

print("linked list is", addTwoNumbers([0], [4,5,6]), "\n \n")

print("linked list is", addTwoNumbers([8,9,2], [4,5,6,9,9]), "\n \n")