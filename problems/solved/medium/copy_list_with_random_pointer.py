# O(N) time complexity as the linked list is iterated through twice. O(N)
# space complexity as we use the original nodes as keys for the old nodes
# so we can know if we have assigned a node already for random node assignment
# to cache out correctly.
def copyRandomList(head):
    """
    given the head of a linked list where nodes point to next or random
    construct a deepy copy. Random pointers can point to any node in the 
    list, or null. 
    """

    if head is None:
        return None

    created = {}

    # create nodes
    curr = head
    while curr:
        created[curr] = Node(curr.val)
        curr = curr.next

    # connect nodes in deep copy
    curr = head
    while curr:
        if curr.next:
            created[curr].next = created[curr.next]
        if curr.random:
            created[curr].random = created[curr.random]
        curr = curr.next

    return created[head]