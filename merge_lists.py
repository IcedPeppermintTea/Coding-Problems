"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy listNode variable
        current = dummy

        while list1 and list2:
            if list1.val < list2.val: # if the value im list1 is smaller than value in list2
                current.next = list1 # appending list1 node to merged list
                list1 = list1.next # move pointer to next node in list1

            else: # if list2 is smaller than list1
                current.next = list2 # append list2 node to merged list
                list2 = list2.next # move pointer to next node in list2
            current = current.next # advance pointer to next node in merged list

        # this loop goes on until the end of the lists

        # after one list is exhausted, attach remaining items from other list
        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next # points to first node in merged list



