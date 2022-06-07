class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2)< len(s1): return False
        
        #Get counts using hash
        h1 = [0] *26
        h2 =[0]*26
        
        for i in range(len(s1)):
            h1[ord(s1[i]) -ord('a')] +=1
            h2[ord(s2[i]) -ord('a')] +=1
        
#       save us from comparing each variable in our count arrays
        matches = 0
        for i in range(26):
            matches += (1 if h1[i]==h2[i] else 0)
#       every pass we find the index of the new char for both pointers, iterate its count in their perspective hash, and ask if the counts between them match to update our match counter variable
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            h2[index] += 1
            if h2[index] == h1[index]:
                matches +=1
            elif h2[index] == h1[index] +1:
                matches -=1
            
            index = ord(s2[l]) - ord('a')
            h2[index] -= 1
            if h2[index] == h1[index]:
                matches +=1
            elif h2[index] == h1[index] -1:
                matches -=1
            l+=1
        return matches == 26