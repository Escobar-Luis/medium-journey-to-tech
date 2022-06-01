class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         Sorting the word or Matching the counts
#         O(n log n), hash, every pass we sort the word and ask if that sorted word is in our hash, if it is we append the original word and if not we create it, at the end we return all the values of the hash
#         O(m*n), hash, every pass we create arr of 26 0s which is our key, then we loop through every word in the str, calulate its index in our arr by subtracting the ord(a)- ord(c), and we iterate the count at the index in our array, then outside that nested loop we set the modified arr containing our counts as a key in our hash and append the word that made that key
        h = collections.defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            h[sorted_word].append(word)
        return h.values()