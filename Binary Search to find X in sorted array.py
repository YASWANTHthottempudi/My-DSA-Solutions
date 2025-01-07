class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        if (len(nums)==1 or len(nums)==2) and (target in nums):
            return nums.index(target)
        else:
            return -1

        return -1
        
