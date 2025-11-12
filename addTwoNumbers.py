# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head 
        c = 0
        while l1 is not None and l2 is not None:
            v1 = l1.val if l1 else 0
            v2=l2.val if l2 else 0
            s= v1+v2+c
            c= s//10
            temp.next = ListNode(s%10)
            l1= l1.next
            l2= l2.next
            temp=temp.next
        while l1 is not None:
            v1 = l1.val if l1 else 0
            s = c+ v1
            c= s//10
            temp.next = ListNode(s%10)
            l1=l1.next
            temp=temp.next
        while l2 is not None:
            v2 = l2.val if l2 else 0
            s = c+ v2
            c= s//10
            temp.next = ListNode(s%10)
            l2=l2.next
            temp=temp.next
        if c:
            temp.next = ListNode(c)
        return head.next
