# prefix tree with wildcard search
class Node:
    def __init__(self, isEnd = False):
        self.terminals = {}
        self.is_end = isEnd

class WordDictionary:
    def __init__(self):
        self.initial = Node()

    def addWord(self, word):
        current = self.initial
        
        for char in word:
            if char not in current.terminals:
                current.terminals[char] = Node()
            current = current.terminals[char]
        
        current.is_end = True

    def search(self, word, current = None):
        if current is None:
            current = self.initial

        for i, char in enumerate(word):
            if char == ".":
                return any(self.search(word[i+1:], key) for key in current.terminals.values())
            if char not in current.terminals:
                return False

            current = current.terminals[char]
        
        return current.is_end

word_dict = WordDictionary()

print(word_dict.addWord("bma"),

      word_dict.addWord("bae"),

      word_dict.addWord("bad"),

      word_dict.search("pad"),

      word_dict.search("ba"),
      
      word_dict.search(".ad"),
      
      word_dict.search("b.d"))
