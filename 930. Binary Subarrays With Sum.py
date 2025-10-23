class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def func(goal):
            if goal<0:
                return 0
            left=0
            right=0
            su=0
            count=0

            while right<len(nums):
                su=su+nums[right]

                while su>goal:
                    su=su-nums[left]
                    left+=1
                
                count=count+right-left+1

                right+=1
            return count
        return func(goal)-func(goal-1)
