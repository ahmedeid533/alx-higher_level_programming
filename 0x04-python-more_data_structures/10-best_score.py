#!/usr/bin/python3
def best_score(a_dictionary):
    if not list(a_dictionary):
        return None
    max_k = list(a_dictionary)[0]
    max_v = a_dictionary[max_k]
    for k, i in a_dictionary.items():
        if i > max_v:
            max_k = k
            max_v = i
    return max_k
