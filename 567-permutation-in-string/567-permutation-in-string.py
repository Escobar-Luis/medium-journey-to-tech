class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        
        h1, h2 = [0]*26, [0]*26
        
        for i in range(len(s1)):
            h1[ord(s1[i])-ord('a')] +=1
            h2[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches +=1 if h1[i] == h2[i] else 0
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches ==26: return True
            
#             find ord value of character
            ind = ord(s2[r]) - ord('a')
            h2[ind] +=1
            if h2[ind] == h1[ind]:
                matches +=1
            elif h2[ind] -1 == h1[ind]:
                matches -=1
            
            ind = ord(s2[l]) - ord('a')
            h2[ind] -=1
            if h2[ind] == h1[ind]:
                matches +=1
            elif h2[ind] + 1 == h1[ind]:
                matches -=1
            l+=1
        return matches == 26
            
            