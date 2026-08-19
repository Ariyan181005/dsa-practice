from collections import defaultdict
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(set)
        for r, s in reservedSeats:
            rows[r].add(s)
        ans = (n - len(rows)) * 2
        for seats in rows.values():
            lt = not ({2, 3, 4, 5} & seats)
            mid = not ({4, 5, 6, 7} & seats)
            rt = not ({6, 7, 8, 9} & seats)
            if lt and rt:
                ans += 2
            elif lt or mid or rt:
                ans += 1
        return ans