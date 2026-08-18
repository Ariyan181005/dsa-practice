class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in grp:
                grp[k] = []
            grp[k].append(s)
        return list(grp.values())