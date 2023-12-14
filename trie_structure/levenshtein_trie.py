import time
import sys
from trie_structure.trie import TrieNode
""" Code is modification from http://stevehanov.ca/blog/?id=114 and paper 10.1109/ISRITI56927.2022.10053062 """
class LevenshteinTrie:
    def __init__(self, dict_path):
        self.trie = TrieNode()
        self._dict = self.convert_trie(dict_path)
        

    def convert_trie(self, path):
        for word in open(path, "rt").read().split():
            self.trie.insert( word )

    

    def search(self, word, maxCost):
        word = word.lower()
        currentRow = range( len(word) + 1 )
        

        results = []

        for letter in self.trie.children:
            self.searchRecursive( self.trie.children[letter], letter, word, currentRow, 
                results, maxCost )
        

        return results


    def searchRecursive(self, node, letter, word, previousRow, results, maxCost ):
        columns = len( word ) + 1
        currentRow = [ previousRow[0] + 1 ]


        for column in range( 1, columns ):

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                replaceCost = previousRow[ column - 1 ] + 1
            else:                
                replaceCost = previousRow[ column - 1 ]

            currentRow.append( min( insertCost, deleteCost, replaceCost ) )

        if currentRow[-1] <= maxCost and node.word != None:
            results.append( (node.word, currentRow[-1] ) )
        

        if min( currentRow ) <= maxCost:
            for letter in node.children:
                self.searchRecursive( node.children[letter], letter, word, currentRow, 
                    results, maxCost )
        
    def get_candidates(self, typo, max_cost):
        candidates = self.search(typo, max_cost)
        sorted_candidates = sorted(candidates, key=lambda item: (item[1], len(item), item[0]))
        
        candidate_words = [candidate[0] for candidate in sorted_candidates]
        
        return candidate_words