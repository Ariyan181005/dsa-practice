class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        a=0
        for i in range(len(s)):
            if i+1 < len(s) and l[s[i]]<l[s[i+1]]:
                a-= l[s[i]]
            else:
                a+= l[s[i]]
        return a 