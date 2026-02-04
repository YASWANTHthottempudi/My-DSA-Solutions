class Solution:
    #Sliding window
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        maxi=0
        zeros=0
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        
        
