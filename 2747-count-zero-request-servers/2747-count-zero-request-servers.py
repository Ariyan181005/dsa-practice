class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x:x[1])
        ids = sorted(range(len(queries)), key = lambda i:queries[i])
        ans = [0]*len(queries)
        cnt = [0]*(n+1)
        beg = 0
        end = 0
        active = 0
        for i in ids:
            q = queries[i]
            while end<len(logs) and logs[end][1]<=q:
                id = logs[end][0]
                if cnt[id]==0:
                    active+=1
                cnt[id]+=1
                end+=1           
            while  beg<end and logs[beg][1]<q-x:
                id = logs[beg][0]
                cnt[id]-=1
                if cnt[id]==0:
                    active-=1
                beg+=1
            ans[i] = n-active        
        return ans