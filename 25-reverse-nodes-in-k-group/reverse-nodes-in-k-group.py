class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes remaining
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Save the next group starting point
            group_next = kth.next

            # Reverse the k nodes: standard pointer reversal
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect group_prev to the new head of the reversed group
            new_group_head = kth
            new_group_tail = group_prev.next

            group_prev.next = new_group_head
            group_prev = new_group_tail