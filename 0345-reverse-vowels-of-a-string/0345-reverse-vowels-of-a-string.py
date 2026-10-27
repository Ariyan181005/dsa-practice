class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        s=list(s)
        low = 0
        high = len(s)-1
        while( low < high):
            if s[low] not in v:
                low+=1
            elif s[high] not in v:
                high -=1
            else:
                s[low],s[high]=s[high],s[low]
                low+=1
                high-=1
        return "".join(s)