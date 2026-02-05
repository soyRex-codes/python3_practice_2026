"""
Here is my solution for Group Anagrams problem.
FIRST group Anagrams problem: It is a condition where there are multiple words that are made up of
exact same letters but in different orders, e.g. eat, tea, ate.
solution approach in pseudocode:
1. we are given a list or hashmap of strings.
1.1. we will sort the letters in each word in alphabet order.
2. we will run a loop to iterate through all the words in the list,
2.1. 2. we will run another loop to iterate through all the letters in each word being processed,
3. inside the loop, we will place logical condition to check each word's letters
with other words letters stored in the Hashmap to identify which words are anagrams of each other.
4. Once match is found we will group anagrams in a hashmap.


Complexity:
Time Complexity: O(N. K log K
Space Complexity: O(N.K)
Scalability: Slower if words are very long (e.g., DNA sequences).,
Better alternativeL instead use Frequency Count Method (Optimal) it gives O(N.K) (Linear!) time complexity.
"""

from collections import defaultdict

# sample data:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def hashmap_pattern(strs):

    hash_map = defaultdict(list) #to store elements in a List and dictionary {key is sorted word : value is original word}

    for word in strs:
        #A. LOGIC: Creates the "Signature"
        # sort "eat" -> ['a', 'e', 't'] -> join -> aet
        sorted_words = "".join(sorted(word)) # sorting word letters in alphabet order

        #B. Storage: Group them
        #because we used defaultdict(list) , we don't need to check if key in map.
        #It automatically creates an empty list if key is new.
        hash_map[sorted_words].append(word)
    return list(hash_map.values())

Sample_data = ["eat", "tea", "tan", "ate", "nat", "bat"] #input is a set, cant use it as a dict
print(hashmap_pattern(Sample_data))