class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    
    ptrA, ptrB = headA, headB
    
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    
    return ptrA

def create_intersected_lists(intersect_val, listA_vals, listB_vals, skipA, skipB):
    if not listA_vals or not listB_vals:
        return None, None
    
    dummyA, dummyB = ListNode(), ListNode()
    currA, currB = dummyA, dummyB
    intersect_node = None
    
    for i, val in enumerate(listA_vals):
        new_node = ListNode(val)
        currA.next = new_node
        currA = new_node
        if i == skipA:
            intersect_node = new_node
    
    for i, val in enumerate(listB_vals):
        new_node = ListNode(val if i < skipB else intersect_val)
        currB.next = new_node
        currB = new_node
        if i == skipB:
            currB.next = intersect_node  
            break
    
    return dummyA.next, dummyB.next

listA_vals = [4,1,8,4,5]
listB_vals = [5,6,1,8,4,5]
headA, headB = create_intersected_lists(8, listA_vals, listB_vals, 2, 3)
print(getIntersectionNode(headA, headB).val if getIntersectionNode(headA, headB) else None)
