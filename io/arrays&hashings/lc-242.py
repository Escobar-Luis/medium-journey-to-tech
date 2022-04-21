class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Base case if the string lengths are not the same
        if len(s) != len(t):
            return False
        #Initiate hash map to populate wit each letter and its count
        hs,ht = {},{}
        for i in range(len(s)):
#             we use range and i so we could access the values of BOTH strings in same for loop
#           We use get method on hash so if the value is not found then python won't throw an error
            hs[s[i]] = 1 + hs.get(s[i],0)
            ht[t[i]] = 1 + ht.get(t[i],0)
        for key in hs:
            if hs[key] != ht.get(key,0):
                return False
        return True