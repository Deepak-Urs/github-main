/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

const reverseLinkedList = (head) => {
    let [prev, curr, next] = [null, head, null]

    while(curr) {
        next = curr.next
        node.next = prev
        prev = node
        node = next
    }

    return prev
}

reverseLinkedList([1,2,3,4,5])