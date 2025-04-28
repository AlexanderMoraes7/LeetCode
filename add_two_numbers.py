"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        carry = 0
        
        for i in reversed(l1):
            node1 = ListNode(i)
            node1.next = first
            first = node1
        first = None
        for j in reversed(l2):
            node2 = ListNode(j)
            node2.next = first
            first = node2
        l1 = node1
        l2 = node2
        first = None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = (l2.val if l2 else 0) + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = (val1 + val2) // 10
            digit = (val1 + val2) % 10
            self.total = ListNode(digit)
            self.total.next = first
            first = self.total
        # return self.total # This was the return on leetcode
        
        return self.print_all()
    
    def print_all(self):
        '''
        I needed to create this method to show all the numbers on vscode,
        but on leetcode shows automatically how list linked just with return
        '''
        result = []
        while self.total != None:
            result.append(self.total.val)
            self.total = self.total.next
        print(result)


s = Solution()
s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])     # Output: [8,9,9,9,0,0,0,1]
s.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])    # Output: [7,0,8]
s.addTwoNumbers(l1 = [0], l2 = [0])            # Output: [0]
