class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):                   # Loop through each element in nums using index i
            for j in range(i+1,len(nums)):           # Loop through remaining elements after i
                if nums[i]  + nums[j] == target:     # Check if sum of nums at i and j equals target
                    return [i,j]                     # Return indices if condition is satisfied
        return []                                    #Return empty index