'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes
of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = temp = ListNode(0)
        # while l1 & l2 are not None
        while l1 and l2:
            # check the vals and append the lesser value to curr
            # advance the pointer of curr and the chose list val
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            # advance curr
            curr = curr.next
        # set the next of curr to the remainder of the list
        # depending on which one was last chosen
        curr.next = l1 if l1 else l2
        '''
        l1 if l1 else l2 is the same as:
        
            if l1 is not None:
                curr.next = l1
            elif l2 is not None:
                curr.next = l2
        '''

        return temp.next
