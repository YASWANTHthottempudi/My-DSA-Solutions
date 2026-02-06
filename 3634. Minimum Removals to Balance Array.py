class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        right=0
        maxi=0
        for left in range(0,n):
            while right<n and nums[right]<=nums[left]*k:
                right+=1

            maxi = max(maxi, right-left)

        return n-maxi

        
