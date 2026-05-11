class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums=[str(i) for i in nums]
        res="".join(nums)
        res=[int(i) for i in res]
        return list(res)
