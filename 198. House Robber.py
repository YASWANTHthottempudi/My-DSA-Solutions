class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(index, dp):
            if index==0:
                return nums[index]
            if index<0:
                return 0

            if dp[index]!=-1:
                return dp[index]

            not_pick= 0+help(index-1, dp )
            pick = nums[index]+help(index-2, dp)

            dp[index] = max(pick, not_pick)
            return dp[index]
        
        dp=[-1]*len(nums)
        return help(len(nums)-1,dp)
