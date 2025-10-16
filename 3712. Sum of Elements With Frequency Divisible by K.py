class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        su=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in nums:
            if d[i]%k==0:
                su+=i
        return su

        
