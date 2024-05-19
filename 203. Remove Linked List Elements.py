class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        current = head

        # Second loop
        while current:
            while current and current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return head