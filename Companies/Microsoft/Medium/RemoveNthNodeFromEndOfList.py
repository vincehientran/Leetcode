# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ret = head
        
        end = head
        nodeToRemove = head
        prevNode = None
        
        while n > 0:
            end = end.next
            n -= 1
            
        while end:
            end = end.next
            prevNode = nodeToRemove
            nodeToRemove = nodeToRemove.next
            
        if prevNode:
            prevNode.next = nodeToRemove.next
            return ret
        else:
            return nodeToRemove.next
            
        
        