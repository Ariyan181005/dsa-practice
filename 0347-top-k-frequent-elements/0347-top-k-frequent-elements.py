class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        ans=[]
        dic={}
        for i in nums:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(k):
            mx = 0
            ele = 0
            for j in dic:
                if dic[j] > mx:
                    mx = dic[j]
                    ele = j
            ans.append(ele)
            del dic[ele]
        return ans
        """
        counter = Counter(nums)
        sorted_arr = sorted(counter, key = lambda x: (counter[x], x), reverse = True)
        return sorted_arr[:k]