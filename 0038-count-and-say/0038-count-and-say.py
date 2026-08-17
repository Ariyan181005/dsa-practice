class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        for i in range(n-1):
            a=""
            i=0
            while i<len(s):
                c = 1
                while i+1<len(s) and s[i]==s[i+1]:
                    c+=1
                    i+=1
                a+=str(c)+s[i]
                i+=1
            s=a
        return s