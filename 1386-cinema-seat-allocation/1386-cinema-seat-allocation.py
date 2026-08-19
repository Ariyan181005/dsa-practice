class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = {}
        for r, s in reservedSeats:
            if r not in reserved:
                reserved[r] = set()
            reserved[r].add(s)
        result = (n - len(reserved)) * 2
        for seats in reserved.values():
            lt = all(s not in seats for s in [2, 3, 4, 5])
            mid = all(s not in seats for s in [4, 5, 6, 7])
            rt = all(s not in seats for s in [6, 7, 8, 9])
            if lt and rt:
                result += 2
            elif lt or mid or rt:
                result += 1
        return result