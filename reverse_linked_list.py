# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        output = ListNode(head.val)
        head = head.next
        while head != None:
            output = ListNode(head.val, output)
            head = head.next
        return output
        