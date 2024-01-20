#https://leetcode.com/problems/linked-list-cycle-ii/description/

def findStartOfLoop(head):
    if head == None or head.next == None:
        return None
    
    s = head
    f = head
    e = head

    while f and f.next:
        s = s.next
        f = f.next.next

        if f == s:
            while s != e:
                s = s.next
                e = e.next
            return True
    
    return False
