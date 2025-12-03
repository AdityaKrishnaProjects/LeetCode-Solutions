# Implement minstack with a graph
class MinStack:
    class NodeStack:
        def __init__(self, val = float("inf"), *, next = None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev
            if prev:
                self.nodeMin = min(prev.nodeMin, self.val)
            else:
                self.nodeMin = self.val

    def __init__(self):
        self.curr = self.NodeStack()
    
    def push(self, val):
        new = self.NodeStack(val, prev = self.curr)
        self.curr.next = new
        self.curr = new

    def pop(self):
        new = self.curr.prev
        new.next = None
        self.curr = new

    def top(self):
        return self.curr.val

    def getMin(self):
        return self.curr.nodeMin

s = MinStack()

s.push(-2)

s.push(0)

s.push(-3)

print(s.getMin())

s.pop()

print(s.top())

print(s.getMin())