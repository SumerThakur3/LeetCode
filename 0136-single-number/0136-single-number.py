
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        xor=0

        for num in nums:
            xor = xor ^ num  #a^a=0 , a^0=a

        return xor    