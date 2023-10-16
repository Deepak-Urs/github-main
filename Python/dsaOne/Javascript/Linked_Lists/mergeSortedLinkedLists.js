//https://leetcode.com/problems/merge-two-sorted-lists/
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

function mergeSortedLinkedListsLists(a, b) {
    let sentinel = tail = new SinglyLinkedList()
    
    while(a && b) {
        const firstG = a.val <= b.val
        const secondG = a.val > b.val

        if(firstG) {
            tail.next = a
            a = a.next
        }

        if(secondG) {
            tail.next = b
            b = b.next
        }

        tail = tail.next
    }

    tail.next = a || b
    
    return sentinel.next
}

mergeSortedLinkedListsLists(a,b)