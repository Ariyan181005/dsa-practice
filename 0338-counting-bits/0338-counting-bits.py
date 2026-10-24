class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0,1,1,2]
        i = 2
        while n > 2**i -1:
            temp = [i +1 for i in dp]
            dp.extend(temp)
            i+=1
        return dp[:n+1]