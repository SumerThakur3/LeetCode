class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0

        for money in nums:

            current=max(
                prev1,          #don't rob this house
                prev2+money     #rob this house
            )

            prev2 = prev1
            prev1 = current

        return prev1    
