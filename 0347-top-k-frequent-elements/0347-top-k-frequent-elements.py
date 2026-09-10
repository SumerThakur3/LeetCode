class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=Counter(nums)
        num1=sorted(num.items(), key=lambda x: x[1], reverse=True)

        return [key for key,value in num1[:k]]

        