class Solution(object):
    def reverseList(self, head):

        current = head
        previous = None

        while current:
            holder = current.next
            current.next = previous

            previous = current
            current = holder

        return previous
