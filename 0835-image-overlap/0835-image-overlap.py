class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        d = {}
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    for x in range(n):
                        for y in range(n):
                            if img2[x][y] == 1:
                                a = i - x
                                b = j - y

                                if (a,b) not in d:
                                    d[(a,b)] = 0

                                d[(a,b)] += 1
        if d:
            return max(d.values())
        return 0