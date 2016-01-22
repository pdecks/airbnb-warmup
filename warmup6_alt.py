"""Suffix Similarities:

1. Create Trie and Trie_Node Classes
2. Add all suffixes to Trie --> walk through string, slicing to add to trie

"""

# Complete the function below.

def  StringSimilarity( inputs):
    results = []
    while inputs:
        input = inputs[0]
        inputs = inputs[1:]
        sum_sim = check_suffix_similarity(input)
        results.append(sum_sim)
    return results

    
def check_suffix_similarity(string):
    # walk through all suffixes, starting with full string
    i = 0
    sum_counts = 0
    while i < len(string):
        curr_suffix = string[i:]
        sum_counts += compare_strings(string, curr_suffix)
        i += 1
    #print sum_counts
    return sum_counts


def compare_strings(string1, string2):
    if len(string2) > len(string1):
        raise IndexError('Length of string2 must be less than or equal to length of string1.')
    count = 0
    # walk through strings simultaneously, break when characters differ
    j = 0
    while j < len(string2):
        if string2[j] == string1[j]:
            count += 1
            j += 1
        else:
            return count
    return count

inputs = ['ababaa']