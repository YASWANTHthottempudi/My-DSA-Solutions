class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        def check(index, su):
            if su == K:
                return True
            if index == N or su > K:
                return False
            
            # Include current element
            if check(index + 1, su + arr[index]):
                return True
            
            # Exclude current element
            if check(index + 1, su):
                return True
            
            return False

        return check(0, 0)
