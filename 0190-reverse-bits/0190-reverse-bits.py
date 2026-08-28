class Solution:
    def reverseBits(self, n: int) -> int:
        bc=f"{n:032b}"
        bc=bc[::-1]
        return int(bc,2)