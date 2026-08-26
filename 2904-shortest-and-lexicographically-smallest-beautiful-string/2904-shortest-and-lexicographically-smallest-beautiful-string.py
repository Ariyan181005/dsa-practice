class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=0
        cnt=0
        ans=""
        for r in range(len(s)):
            if s[r]=='1':
                cnt+=1
            while cnt==k:
                temp=s[l:r+1]
                if ans == "" or len(temp)<len(ans) or (len(temp)==len(ans) and temp<ans):
                    ans=temp
                if s[l]=='1':
                    cnt-=1
                l+=1
        return ans