class Solution:
    def count(self, head, key):
        current = head
        count = 0
        while (current is not None):
            if current.data == key:
                count += 1
            current = current.next
        return count