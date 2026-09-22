class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [[0] * k for _ in range(4 * n)]
        prod = [1] * (4 * n)
        def merge(p1, c1, p2, c2):
            p = (p1 * p2) % k
            c = c1[:]
            for i in range(k):
                c[(p1 * i) % k] += c2[i]
            return p, c
        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                prod[node] = v
                tree[node][v] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            prod[node], tree[node] = merge(prod[node * 2],tree[node * 2],prod[node * 2 + 1],tree[node * 2 + 1])
        def update(node, l, r, pos, val):
            if l == r:
                v = val % k
                tree[node] = [0] * k
                tree[node][v] = 1
                prod[node] = v
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(node * 2, l, mid, pos, val)
            else:
                update(node * 2 + 1, mid + 1, r, pos, val)
            prod[node], tree[node] = merge(prod[node * 2],tree[node * 2],prod[node * 2 + 1],tree[node * 2 + 1])
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], tree[node][:]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            p1, c1 = query(node * 2, l, mid, ql, qr)
            p2, c2 = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(p1, c1, p2, c2)
        build(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            p, cnt = query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])
        return ans