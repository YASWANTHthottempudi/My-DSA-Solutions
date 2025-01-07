class Solution:
    def findKRotation(self, nums):
        # code here
        if len(nums)==0:
            return 0
        mini=0
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=nums[low]:
                if nums[low]>=nums[high]:
                    if mid>0 and nums[mid]<nums[mid-1]:
                        mini=mid
                        break
                    low=mid+1

                else:
                    if mid>0 and nums[mid]<nums[mid-1]:
                        mini=mid
                        break
                    high=mid-1
            else:
                if nums[mid]<=nums[high]:
                    if mid>0 and nums[mid]<nums[mid-1]:
                        mini=mid
                        break
                    high=mid-1
                else:
                    if mid>0 and nums[mid]<nums[mid-1]:
                        mini=mid
                        break
                    low=mid+1

        return mini       
