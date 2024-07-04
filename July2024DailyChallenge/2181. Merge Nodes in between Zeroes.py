#Time Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next
        tot = 0
        while r:
            if r.val != 0:
                tot += r.val
            else:
                l = l.next
                l.val = tot
                tot = 0
            r=r.next
        l.next = None

        return head.next
