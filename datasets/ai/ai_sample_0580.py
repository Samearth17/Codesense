class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        """
        Inserts a word into the trie
        """
        curr_node = self.root
        for letter in word:
            # if letter is not in the current branch
            if letter not in curr_node:
                # add letter to the branch
                curr_node[letter] = {}
            # move to the next branch
            curr_node = curr_node[letter]
        # when word is fully parsed, set node name to True
        curr_node['name'] = True