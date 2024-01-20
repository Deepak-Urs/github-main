#https://leetcode.com/problems/linked-list-cycle/description/


def detectLoop(head):
    s = head
    f = head

    while f and f.next:
        s = s.next
        f = f.next.next

        if f == s:
            return True

    return False
