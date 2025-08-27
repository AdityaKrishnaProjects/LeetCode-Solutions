# hash table
def cloneGraph(node):
    
    if not node:
        return

    if not node.neighbors:
        return Node(node.val)

    created = {}
    exhausted = set()

    def search(node):
        
        if node.val in exhausted:
            return
        else:
            if node.val in created:
                curr_node = created[node.val]
            else:
                curr_node = Node(node.val)
                created[node.val] = curr_node

            for neighbor in node.neighbors:
                if neighbor.val in created:
                    curr_node.neighbors.append(created[neighbor.val])
                else:
                    temp = Node(neighbor.val)
                    created[neighbor.val] = temp
                    curr_node.neighbors.append(temp)

            exhausted.add(node.val)

            for neighbor in node.neighbors:
                search(neighbor)

    search(node)
        
    return created[1]