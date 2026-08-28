class Solution:
    def hammingWeight(self, n: int) -> int:
        bc=f"{n:032b}"
        return bc.count('1')