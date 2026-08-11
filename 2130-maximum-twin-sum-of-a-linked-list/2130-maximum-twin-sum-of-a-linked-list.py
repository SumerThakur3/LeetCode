# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle of the list
        slow=head
        fast=head

        while fast:
            slow=slow.next
            fast=fast.next.next

        #Reverse the second half
        previous=None

        while slow:
            next_node=slow.next
            slow.next=previous

            previous=slow
            slow=next_node

        # Find maximum twin sum
        first=head
        second=previous
        max_sum=0

        while second:
            current_sum=first.val+second.val
            max_sum=max(max_sum,current_sum)

            first=first.next
            second=second.next

        return max_sum       