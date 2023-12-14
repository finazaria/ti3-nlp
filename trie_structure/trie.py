# code modified from: http://stevehanov.ca/blog/?id=114
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

        # global NodeCount
        # NodeCount += 1

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word