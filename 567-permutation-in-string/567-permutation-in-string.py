class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)> len(s2): return False
        #count arr
        h1,h2 = [0]*26, [0]*26
        
        for i in range(len(s1)):
            h1[ord(s1[i]) - ord('a')] +=1
            h2[ord(s2[i]) - ord('a')] +=1
            
        matches = 0
        for i in range(26):
            matches += 1 if h1[i]==h2[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            h2[index] +=1
            if h2[index] == h1[index]:
                matches +=1
            elif h2[index] == h1[index]+1:
                matches -=1
            
            index = ord(s2[l]) - ord('a')
            h2[index] -=1
            if h2[index] == h1[index]:
                matches +=1
            elif h2[index] == h1[index]-1:
                matches -=1
            l+=1
            
        return matches == 26
        
        