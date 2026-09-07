class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bu = 0
        s = {}
        g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bu += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        cw = 0
        for x in s:
            if x in g:
                cw += min(s[x], g[x])
        return str(bu) + "A" + str(cw) + "B"