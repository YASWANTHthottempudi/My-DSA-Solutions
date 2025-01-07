class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if (len(nums)==1 or len(nums)==2) and target in nums:
            return True
        elif (len(nums)==1 or len(nums)==2) and target not in nums:
            return False
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and nums[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return False
            
        
