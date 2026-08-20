import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]   
        for num in nums:
            heapq.heappush(heap,num) #it keeps the smallest element at top

            if len(heap) > k:
                heapq.heappop(heap) #it removes the top element(smallest element)

        return heap[0] #because the kth largest element will be at top

