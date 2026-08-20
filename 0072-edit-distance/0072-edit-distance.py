class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        c=[[0]*(len(word2)+1)for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            c[len(word1)][i]=len(word2)-i
        for j in range(len(word1)+1):
            c[j][len(word2)]=len(word1)-j
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    c[i][j]=c[i+1][j+1]
                else:
                    c[i][j]=1+min(c[i+1][j],c[i][j+1],c[i+1][j+1])
        return c[0][0]