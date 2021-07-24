# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = None
        current = None

        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = l1
                    current = l1
                else:
                    current.next = l1
                    current = current.next

                l1 = l1.next

            else:
                if not head:
                    head = l2
                    current = l2
                else:
                    current.next = l2
                    current = current.next

                l2 = l2.next

        if l1:
            if current:
                current.next = l1
            else:
                head = l1

        if l2:
            if current:
                current.next = l2
            else:
                head = l2

        return head

# recursively
'''class Solution(object):
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2'''
