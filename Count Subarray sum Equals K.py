class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)

        if n==0:
            return 0
        elif n==1:
            if nums[0]==k:
                return 1
            else: 
                return 0
        else:
            d={0:1}
            su=0
            count=0
            for i in range(0,len(nums)):
                su=su+nums[i]
                if su-k in d.keys():
                    count=count+d[su-k]
                if su in d.keys():
                    d[su]+=1
                else:
                    d[su]=1
            return count
