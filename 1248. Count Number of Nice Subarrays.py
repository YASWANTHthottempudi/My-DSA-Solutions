class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def func(k):
            if k < 0:
                return 0
            left = 0
            odd_count = 0  # Count of odd numbers (instead of sum)
            count = 0
            
            for right in range(len(nums)):
                # Add 1 if odd, 0 if even
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                # Shrink window while we have too many odd numbers
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                # Count all subarrays ending at right with ≤ k odd numbers
                count += right - left + 1
            
            return count
        
        # Exactly k = at most k - at most (k-1)
        return func(k) - func(k - 1)
