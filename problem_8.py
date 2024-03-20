class node:
    def __init__(data):
        self.data = data
        self.next = None
        
class Solution:
    def findMid(self, head):
        if head is None or head.next is None:
            return head.data
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data