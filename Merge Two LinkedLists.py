class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def mergetwo(l1,l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next
