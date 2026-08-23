class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(spells)
        m=len(potions)
        pair=[0]*n

        for i in range(n):
            spell=spells[i]
            left=0
            right=m-1

            while left <= right:
                mid=(left+right)//2
                product=spell*potions[mid]

                if product >= success:
                    right=mid-1
                else:
                    left=mid+1

            pair[i]=m-left
        
        return pair