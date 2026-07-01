"""
Write an algorithm to implement a trie data structure in Python
"""

class TrieNode(object):
    """Trie node class"""
    def __init__(self):
        """Constructor for trie node"""
        self.children = {}
        self.end_of_word = False

class Trie(object):
    """Trie class"""

    def __init__(self):
        """Constructor for Trie"""
        self.root = TrieNode()

    def insert(self, word):
        """Inserts the given word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.end_of_word = True

    def search(self, word):
        """Searches if the given word is present in the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

# Test code
trie = Trie() 
words = ["apple", "application", "hi"]

# Insert words into the trie
for word in words:
    trie.insert(word)

# Test search
if trie.search("apple"):
    print("Word Found")
else:
    print("Word Not Found")