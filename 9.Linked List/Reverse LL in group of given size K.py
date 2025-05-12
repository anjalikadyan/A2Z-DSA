class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Helper to check if there are at least k nodes left
    def hasKNodes(curr, k):
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        return count == k

    # Helper to reverse k nodes starting from node
    def reverseK(start, k):
        prev = None
        curr = start
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # new head of the reversed group

    dummy = ListNode(0)
    dummy.next = head
    groupPrev = dummy

    while hasKNodes(groupPrev.next, k):
        kth = groupPrev
        for _ in range(k):
            kth = kth.next
        groupNext = kth.next

        # Reverse the k nodes
        prev, curr = groupNext, groupPrev.next
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Connect with previous part
        tmp = groupPrev.next
        groupPrev.next = prev
        groupPrev = tmp

    return dummy.next
