#https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    mid = length//2

    i = 1
    curr = head
    while i <= mid:
        curr = curr.next
        i += 1
    
    return curr


        