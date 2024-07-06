# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        critic_pts = []
        prev = head
        curr = head.next
        pos = 1
        
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                critic_pts.append(pos)
            prev = curr
            curr = curr.next
            pos+=1

        if len(critic_pts)<2:
            return [-1,-1]

        mindis = float('inf')
        maxdis = critic_pts[-1] - critic_pts[0]

        for i in range(1, len(critic_pts)):
            mindis = min(mindis, critic_pts[i] - critic_pts[i-1])

        return [mindis, maxdis]
