import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair=list(zip(nums1,nums2))

        pair.sort(key=lambda x:x[1],reverse=True)

        heap=[]
        total=0
        answer=0
        
        for nums1,nums2 in pair:
            heapq.heappush(heap,nums1)
            total+=nums1

            if len(heap) > k:
                remove=heapq.heappop(heap)
                total-=remove
            if len(heap)==k:
                score=total*nums2
                answer=max(answer,score)    

        return answer        