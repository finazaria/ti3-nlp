"""
Tugas Individu 3
Natural Language Processing
Alfina Azaria - 2006482773
"""

import performance
from trie_structure.levenshtein_trie import LevenshteinTrie
from trie_structure.damerau_levenshtein_trie import DamerauLevenshteinTrie
from dict_structure.levenshtein_dict import LevenshteinDict
from dict_structure.damerau_levenshtein_dict import DamerauLevenshteinDict
import json
import time

""" 
TODO: Hitung akurasi dan Run-Time dari semua algoritma yang sudah disediakan, seperti 
LevenshteinTrie, DamerauLevenshteinTrie, LevenshteinDict, dan DamerauLevenshteinDict. 
Gunakan SALTIK (https://github.com/ir-nlp-csui/saltik) sebagai dataset 
dan atur parameter MAX_COST untuk setiap algoritma sebesar 2 ketika memanggil 
fungsi untuk pengambilan kandidat.
"""
def main():
    return performance.main()

if __name__ == '__main__':
    main()