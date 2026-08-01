class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            rightsum = totalsum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]#Add current element to left sum for next iteration
        return -1    
               