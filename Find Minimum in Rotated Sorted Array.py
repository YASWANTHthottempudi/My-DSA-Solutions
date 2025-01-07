class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mini=99999999
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=nums[low]:
                if nums[low]>=nums[high]:
                    low=mid+1
                    mini=min(mini,nums[mid])
                else:
                    mini=min(mini,nums[mid])
                    high=mid-1
            else:
                if nums[mid]<=nums[high]:
                    high=mid-1
                    mini=min(mini,nums[mid])
                else:
                    low=mid+1
                    mini=min(mini,nums[mid])
        return mini
        
