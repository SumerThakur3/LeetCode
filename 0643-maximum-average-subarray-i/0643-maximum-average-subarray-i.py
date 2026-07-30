class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])        # Sum of first window
        max_sum=window_sum              # Maximum sum found so far
        for i in range(k,len(nums)):
            # Remove left element and add new right element
            window_sum=window_sum-nums[i-k]+nums[i]
            # Update maximum sum
            if window_sum > max_sum:
                max_sum=window_sum
        return max_sum/float(k)        

