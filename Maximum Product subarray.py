class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        maxi=-9999999
        for i in range(0,len(nums)):

            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-i-1]
            maxi=max(maxi,prefix,suffix)
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
        return maxi
