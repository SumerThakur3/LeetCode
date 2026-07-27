class Solution:
    def increasingTriplet(self, num: List[int]) -> bool:
        first=float('inf') #first smallest number
        #float('inf') means positive infinity.
        second=float('inf') #second smallest number
        for i in range(len(num)):
            if num[i]<=first:
                first=num[i]
            elif num[i]<=second:
                second=num[i]
            else:
                return True   #first < second < num[i]
        return False                              