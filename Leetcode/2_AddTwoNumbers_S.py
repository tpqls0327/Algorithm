# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        cur = node
        carry = 0
        while l1 or l2 or carry:    # 예제 3번처럼 승수만 뒤로 넘겨지는 경우도 있으니 carry를 조건에 추가
            if l1:
                carry += l1.val
                l1 = l1.next 
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)    # 나머지 저장
            cur = cur.next
            carry = carry // 10    # 몫 저장
        return node.next
