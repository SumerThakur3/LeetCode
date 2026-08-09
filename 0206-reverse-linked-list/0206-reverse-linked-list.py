# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=None
        current=head

        while current:
            #Save the next node
            next_node=current.next

            #Reverse the link (means if current=1 then current.next=None)
            current.next=previous

            #Move previous and Move current(previous was none now it moves to 1)
            previous=current
            current=next_node

        return previous    
