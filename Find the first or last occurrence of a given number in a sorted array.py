class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        index=-1
        index2=-1
        index1=-1
        while (low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                index=mid
                break
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        if index==-1:
            return [-1,-1]
        low=0
        high=index
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                index1=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        low=index
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                index2=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        return [min(index,index1,index2),max(index,index1,index2)]



        
