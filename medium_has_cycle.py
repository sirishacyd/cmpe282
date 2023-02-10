class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def has_cycle(head):
    if head is None:
        return 0

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1

    return 0
