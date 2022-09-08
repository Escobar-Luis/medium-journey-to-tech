class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = collections.defaultdict(list)
        for s in strs:
            sort = ''.join(sorted(s))
            h[sort].append(s)
        return h.values()