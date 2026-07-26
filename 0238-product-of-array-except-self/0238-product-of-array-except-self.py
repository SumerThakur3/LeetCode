class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n  #list for storing answer i.e ex:[1,1,1,1] (multiply operation)
        prefix=1
        for i in range(n):
            answer[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]    
        return answer    