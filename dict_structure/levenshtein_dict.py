import time
import sys
from Levenshtein import distance

""" Code is modification from http://stevehanov.ca/blog/?id=114 and paper 10.1109/ISRITI56927.2022.10053062 """
class LevenshteinDict:
    def __init__(self, dict_path):
        self._kbbi = self.convert_dict(dict_path)
        
    def convert_dict(self, path):
        # convert KBBI into Dict structure --> {'word':1}, 1 just dummy number
        kbbi_dict = {line.split()[0] : 1 for line in open(path)} 
        return kbbi_dict
        

    def search(self, typo, maxCost ):
        results = []
        for candidate_word in self._kbbi.keys():
            cost = distance( typo, candidate_word )

            if cost <= maxCost:
                results.append( (candidate_word, cost) )
        return results
    
    def get_candidates(self, typo, max_cost):
        candidates = self.search(typo, max_cost)
        sorted_candidates = sorted(candidates, key=lambda item: (item[1], len(item), item[0]))
        candidate_words = [candidate[0] for candidate in sorted_candidates]
        
        return candidate_words