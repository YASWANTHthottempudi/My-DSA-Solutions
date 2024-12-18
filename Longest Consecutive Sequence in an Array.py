class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        d=set()
        for i in nums:
            if i not in d:
                d.add(i)
        count=0
        count1=0
        for i in d:
            if i-1 not in d:
                count=1
                while i+1 in d:
                    i=i+1
                    count=count+1
                count1=max(count,count1)
        return count1
