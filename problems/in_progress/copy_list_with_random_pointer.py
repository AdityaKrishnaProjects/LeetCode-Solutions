# fix random pointer logic, need to use length and distance to end to determine what current index is for key in created 
def copyRandomList(head):
    """
    given the head of a linked list where nodes point to next or random
    construct a deepy copy. Random pointers can point to any node in the 
    list, or null. 
    """

    def distCalculator(node):
        length = 0

        while node is not None:
            length += 1
            node = node.next
        
        return length

    copy = head
    total_length = distCalculator(copy)

    created = {}

    def NodeExplorer(original_node, deep_node, counter):
        deep_node.val = original_node.val
        created[counter] = deep_node

        counter += 1

        # next handler
        if original_node.next is not None:
            if counter in created:
                deep_node.next = created[counter]
            else:
                next_node = Node()
                deep_node.next = next_node
                created[counter] = next_node
                NodeExplorer(original_node.next, next_node, counter)
        else:
            deep_node.next = None

        # random handler
        if original_node.random is not None:
            length = distCalculator(original_node.random)
            if (total_length - length + 1) in created:
                deep_node.random = created[total_length - length + 1]
            else:



    # set pointer to first node in original
    curr = head

    NodeExplorer(curr, Node(), 1)