class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and nums[0]==target:
            return 0
        elif len(nums)==1 and nums[0]!=target:
            return -1
        if len(nums)==2 and target in nums:
            return nums.index(target)
        elif len(nums)==2 and target not in nums:
            return -1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target and nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

  
        return -1
