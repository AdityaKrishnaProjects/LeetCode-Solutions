class Node:
    def __init__(self, isEnd = False):
        self.edges = {}
        self.is_end = isEnd

    def insert(self, ch):
        if not self.has_edge(ch):
            self.edges[ch] = Node()
        return self.edges[ch]

    def has_edge(self, ch):
        return ch in self.edges

    def get(self, ch):
        return self.edges[ch]

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current = self.root

        for ch in word:
            current = current.insert(ch)

        current.is_end = True

    def search(self, word):
        current = self.root

        for ch in word:
            if not current.has_edge(ch):
                return False
            current = current.get(ch)

        return current.is_end

    def startsWith(self, prefix):
        current = self.root

        for ch in prefix:
            if not current.has_edge(ch):
                return False
            current = current.get(ch)

        return True

trie = Trie()

print(trie.insert("apps"))

print(trie.search("apps"))