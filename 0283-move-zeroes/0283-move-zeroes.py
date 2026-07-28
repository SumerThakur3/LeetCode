class Solution:
    def moveZeroes(self, num: List[int]) -> None:
         pos=0  #position to place next non-zero element
         for i in range(len(num)):  #scans every element in the array
             if num[i]!=0:
                num[pos],num[i]=num[i],num[pos]
                pos+=1   