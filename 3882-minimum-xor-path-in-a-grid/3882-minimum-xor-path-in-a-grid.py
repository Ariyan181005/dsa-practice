class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        masks = []

        for b in range(10):
            block = 1 << b
            mask = 0
            base = (1 << block) - 1

            for p in range(block, 1024, 2 * block):
                mask |= base << p

            masks.append(mask)

        def xor_shift(bits, x):
            for b in range(10):
                if (x >> b) & 1:
                    block = 1 << b
                    mask = masks[b]

                    bits = (
                        ((bits & mask) >> block)
                        |
                        ((bits & ~mask) << block)
                    )

            return bits

        prev = [0] * m

        for i in range(n):
            cur = [0] * m

            for j in range(m):
                if i == 0 and j == 0:
                    states = 1
                elif i == 0:
                    states = cur[j - 1]
                elif j == 0:
                    states = prev[j]
                else:
                    states = prev[j] | cur[j - 1]

                cur[j] = xor_shift(states, grid[i][j])

            prev = cur

        states = prev[m - 1]

        return (states & -states).bit_length() - 1