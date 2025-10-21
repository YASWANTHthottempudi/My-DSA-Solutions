import math

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        d={}
        for i in range(len(nums)):
            if i<len(nums)-1:
                if nums[i]==nums[i+1]:
                    return True
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                if math.fabs(d[nums[i]]-i)<=k:
                    return True
        return False
        
