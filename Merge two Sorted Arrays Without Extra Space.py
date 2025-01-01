class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        l=m+n-1
        i=m-1
        j=n-1
        while i>-1 and j>-1:
            if nums2[j]>=nums1[i]:
                nums1[l]=nums2[j]
                j=j-1
            else:
                nums1[l]=nums1[i]
                i=i-1
            l=l-1
        while j>-1:
            nums1[l]=nums2[j]
            j=j-1
            l=l-1
