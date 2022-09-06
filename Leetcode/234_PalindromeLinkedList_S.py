class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        if head is None:
            return True
        
        while head.next != None:
            arr.append(head.val)
            head = head.next
        
        arr.append(head.val)
        
        if arr == arr[::-1]:
            return True
        else: return False
