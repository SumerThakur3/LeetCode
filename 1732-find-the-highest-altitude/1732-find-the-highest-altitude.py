class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current=0
        max_num=0
        for i in range(0,len(gain)):
            current+=gain[i]
            max_num=max(max_num,current)
        return max_num
            