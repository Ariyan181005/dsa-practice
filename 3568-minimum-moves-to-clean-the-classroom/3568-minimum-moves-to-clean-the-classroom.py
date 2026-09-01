from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        lp = []
        sp = (0, 0)
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    sp = (r, c)
                elif classroom[r][c] == 'L':
                    lp.append((r, c))
        tm = (1 << len(lp)) - 1
        if tm == 0:
            return 0
        lm = {pos: i for i, pos in enumerate(lp)}
        q = deque([(0, sp[0], sp[1], 0, energy)])
        vis = {(sp[0], sp[1], 0): energy}
        while q:
            moves, r, c, mask, curen = q.popleft()
            if curen == 0:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                nxten = curen - 1
                nxtm = mask
                if classroom[nr][nc] == 'R':
                    nxten = energy
                if classroom[nr][nc] == 'L':
                    nxtm |= (1 << lm[(nr, nc)])
                if nxtm == tm:
                    return moves + 1
                st = (nr, nc, nxtm)
                if st not in vis or vis[st] < nxten:
                    vis[st] = nxten
                    q.append((moves + 1, nr, nc, nxtm, nxten))
        return -1