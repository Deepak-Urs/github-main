#https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def oddEvenLL(head):
    if not head:
        return None
    elif not head.next:
        return head
    else:
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = even_head

        return head

print(oddEvenLL([1,2,3,4,5]))
print(oddEvenLL([2,1,3,5,6,4,7]))