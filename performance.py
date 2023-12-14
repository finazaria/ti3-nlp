"""
Tugas Individu 3
Natural Language Processing
Alfina Azaria - 2006482773
"""

import sys, time, json

import dict_structure.damerau_levenshtein_dict as dd
import dict_structure.levenshtein_dict as dl

import trie_structure.damerau_levenshtein_trie as td
import trie_structure.levenshtein_trie as tl
import trie_structure.trie as t

"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan run-time
"""
"""
About the Assignment
• There are two types of dataset: Trie and Dict
• and two types of algorithm to calculate distance : Levenshtein Distance & Damerau-Levenshtein Distance
"""
class Performance():
    def __init__(self) -> None:
        self.saltik: dict = None

    def get_saltik(self, path: str) -> dict:
        # Open the JSON file
        with open(path, "r") as f:
            # Read the JSON data
            self.saltik = json.load(f)

        return self.saltik
        
    def get_n(self, dict: dict) -> int:
        n_count = 0
        for key,value in dict.items():
            for dict in value:
                n_count += 1 
        return n_count
    
    def get_m_candidate(self, data: dict, method) -> int:
        # Instantiate
        dict_dam = dd.DamerauLevenshteinDict('TI3-NLP/bahasa-indonesia-dictionary.txt')
        dict_lev = dl.LevenshteinDict('TI3-NLP/bahasa-indonesia-dictionary.txt')

        trie_dam = td.DamerauLevenshteinTrie('TI3-NLP/bahasa-indonesia-dictionary.txt')
        trie_lev = tl.LevenshteinTrie('TI3-NLP/bahasa-indonesia-dictionary.txt')
        trie = t.TrieNode()

        m_candidate = 0 

        if method == "dict_dam":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = dict_dam.get_candidates(typo_word, 2)

                    # Iterate list of candidates
                    for i in list_of_candidates:
                        if i == key:              # If the correct word is included in the list_of_candidates
                            m_candidate += 1

        elif method == "dict_lev":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = dict_lev.get_candidates(typo_word, 2)

                    # Iterate list of candidates
                    for i in list_of_candidates:
                        if i == key:              # If the correct word is included in the list_of_candidates
                            m_candidate += 1

        elif method == "trie_dam":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = trie_dam.get_candidates(typo_word, 2)

                    # Iterate list of candidates
                    for i in list_of_candidates:
                        if i == key:              # If the correct word is included in the list_of_candidates
                            m_candidate += 1

        elif method == "trie_lev":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = trie_lev.get_candidates(typo_word, 2)

                    # Iterate list of candidates
                    for i in list_of_candidates:
                        if i == key:              # If the correct word is included in the list_of_candidates
                            m_candidate += 1
                
        return m_candidate

    def get_m_best_match(self, data: dict, method) -> int:
        # Instantiate
        dict_dam = dd.DamerauLevenshteinDict('TI3-NLP/bahasa-indonesia-dictionary.txt')
        dict_lev = dl.LevenshteinDict('TI3-NLP/bahasa-indonesia-dictionary.txt')

        trie_dam = td.DamerauLevenshteinTrie('TI3-NLP/bahasa-indonesia-dictionary.txt')
        trie_lev = tl.LevenshteinTrie('TI3-NLP/bahasa-indonesia-dictionary.txt')
        trie = t.TrieNode()

        m_best_match = 0

        if method == "dict_dam":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = dict_dam.get_candidates(typo_word, 2)

                    # If the correct word is on the first place in the list_of_candidates
                    if list_of_candidates[0] == key:
                        m_best_match += 1
        
        elif method == "dict_lev":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = dict_lev.get_candidates(typo_word, 2)

                    # If the correct word is on the first place in the list_of_candidates
                    if list_of_candidates[0] == key:
                        m_best_match += 1

        elif method == "trie_dam":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = trie_dam.get_candidates(typo_word, 2)

                    # If the correct word is on the first place in the list_of_candidates
                    if list_of_candidates[0] == key:
                        m_best_match += 1

        elif method == "trie_lev":
            # Iterate dict items
            for key,value in data.items():
                for dict in value:
                    typo_word = dict.get('typo')
                    list_of_candidates = trie_lev.get_candidates(typo_word, 2)

                    # If the correct word is on the first place in the list_of_candidates
                    if list_of_candidates[0] == key:
                        m_best_match += 1
                
        return m_best_match

    def print_results(self, nama, npm, results):
        print(f"[ {nama} - {npm} ]")
        for method, metrics in results.items():
            print(f"---------- {method} ----------")
            print(f"best accuracy : {metrics['best_accuracy']}")
            print(f"candidate accuracy : {metrics['candidate_accuracy']}")
            print(f"total_time : {metrics['total_time']}")

def main():
    print("Creating instance ... ")
    performance = Performance()
    print("Instance created")
    print("---------------------")

    # Read SALTIK
    print("Importing SALTIK ...")
    saltik = performance.get_saltik('TI3-NLP/saltik_200.json')
    print("SALTIK imported")
    print("---------------------")

    n_count = performance.get_n(saltik)

    # lev_trie
    print("Running Levenshtein Trie ...")
    start_time_lev_trie = time.time()
    lev_trie_m_candidate = performance.get_m_candidate(saltik, "trie_lev")
    lev_trie_m_best_match = performance.get_m_best_match(saltik, "trie_lev")
    end_time_lev_trie = time.time()
    
    res_lev_trie_candidate = lev_trie_m_candidate / n_count
    res_lev_trie_best_match = lev_trie_m_best_match / n_count
    runtime_lev_trie = end_time_lev_trie - start_time_lev_trie
    print("Finished Running Levenshtein Trie")
    print("---------------------")

    # dalev_trie
    print("Running Damerau-Levenshtein Trie ...")
    start_time_dalev_trie = time.time()
    dalev_trie_m_candidate = performance.get_m_candidate(saltik, "trie_dam")
    dalev_trie_m_best_match = performance.get_m_best_match(saltik, "trie_dam")
    end_time_dalev_trie = time.time()

    res_dalev_trie_candidate = dalev_trie_m_candidate / n_count
    res_dalev_trie_best_match = dalev_trie_m_best_match / n_count
    runtime_dalev_trie = end_time_dalev_trie - start_time_dalev_trie
    print("Finished Running Damerau-Levenshtein Trie")
    print("---------------------")

    # lev_dict
    print("Running Levenshtein Dictionary ...")
    start_time_lev_dict = time.time()
    lev_dict_m_candidate = performance.get_m_candidate(saltik, "dict_lev")
    lev_dict_m_best_match = performance.get_m_best_match(saltik, "dict_lev")
    end_time_lev_dict = time.time()
    
    res_lev_dict_candidate = lev_dict_m_candidate / n_count
    res_lev_dict_best_match = lev_dict_m_best_match / n_count
    runtime_lev_dict = end_time_lev_dict - start_time_lev_dict
    print("Finished Running Levenshtein Dictionary")
    print("---------------------")

    # dalev_dict
    print("Running Damerau-Levenshtein Dictionary ...")
    start_time_dalev_dict = time.time()
    print("Running Damerau-Levenshtein Dictionary: Getting M Candidate ... ")
    dalev_dict_m_candidate = performance.get_m_candidate(saltik, "dict_dam")
    print("Running Damerau-Levenshtein Dictionary: Getting M Best Match ...")
    dalev_dict_m_best_match = performance.get_m_best_match(saltik, "dict_dam")

    print("Finished Getting All M-Score")
    end_time_dalev_dict = time.time()
    
    res_dalev_dict_candidate = dalev_dict_m_candidate / n_count
    res_dalev_dict_best_match = dalev_dict_m_best_match / n_count
    runtime_dalev_dict = end_time_dalev_dict - start_time_dalev_dict
    print("Finished Running Damerau-Levenshtein Dictionary")
    print("---------------------")


    # Print result metrics
    nama = "Alfina Azaria"
    npm = "2006482773"
    results = {
        'lev_trie': {'best_accuracy': res_lev_trie_best_match, 'candidate_accuracy': res_lev_trie_candidate, 'total_time': runtime_lev_trie},
        'dalev_trie': {'best_accuracy': res_dalev_trie_best_match, 'candidate_accuracy': res_dalev_trie_candidate, 'total_time': runtime_dalev_trie},
        'lev_dict': {'best_accuracy': res_lev_dict_best_match, 'candidate_accuracy': res_lev_dict_candidate, 'total_time': runtime_lev_dict},
        'dalev_dict': {'best_accuracy': res_dalev_dict_best_match, 'candidate_accuracy': res_dalev_dict_candidate, 'total_time': runtime_dalev_dict}
    }

    # Print the results
    performance.print_results(nama, npm, results)


if __name__ == "__main__":
    main()