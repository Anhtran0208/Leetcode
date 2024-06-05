"""
Problem: 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode()
        curr = dummyNode
        while l1 or l2 or carry != 0:
            curr1 = l1.val if l1 else 0
            curr2 = l2.val if l2 else 0
            total = curr1 + curr2 + carry 
            carry = total // 10
            new_node = ListNode(total % 10)
            curr.next = new_node
            curr = new_node
            #next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyNode.next
