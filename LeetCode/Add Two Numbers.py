# 2014-01-14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# main code
class Solution(object):

    # main def
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1_int = self.to_int(l1)
        l2_int = self.to_int(l2)
        
        res_str = str(l1_int+l2_int)[::-1]
        
        return self.to_lkdlist(res_str)

    # linked list to reversed int num
    def to_int(self, lkdlst):
        lkdlst_str = ""
        while lkdlst:
            lkdlst_str += str(lkdlst.val)
            lkdlst = lkdlst.next
            
        lkdlst_int = int(lkdlst_str[::-1])
        
        return lkdlst_int

    # int num to linked list 
    def to_lkdlist(self, string):
        head = prev = None
        for ele in string:
            node = ListNode(ele)
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
        
        return head
    

    
    
