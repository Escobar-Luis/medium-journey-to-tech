class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2): return False
        
        oc = [0] * 26
        dc = [0] * 26
        
#       populating first counts
        for i in range(len(s1)):
            oc[ord(s1[i]) - ord('a')] +=1
            dc[ord(s2[i]) - ord('a')] +=1
            
        matches = 0
        for i in range(26):
            if oc[i] == dc[i]:
                matches += 1
            else:
                continue
            
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            
            ind = ord(s2[r]) - ord('a')
            dc[ind] +=1
            if oc[ind] == dc[ind]:
                matches +=1
            elif oc[ind] +1 == dc[ind]:
                matches -=1
                
            ind = ord(s2[l]) - ord('a')
            dc[ind] -=1
            if oc[ind] == dc[ind]:
                matches +=1
            elif oc[ind] -1 == dc[ind]:
                matches -=1
            l+=1
        return matches == 26