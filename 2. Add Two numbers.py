class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def l_to_n(list_node):
            s = ""
            while list_node:
                s += str(list_node.val)
                list_node = list_node.next
            return int(s[::-1])
    
        def n_to_l(num):
            n_reverse = list(map(int, str(num)[::-1]))
            list_node = ListNode() 
            now = list_node 
            for n in n_reverse:
                now.next = ListNode(val = n) 
                now = now.next 
            return list_node.next
            
        return n_to_l(l_to_n(l1) + l_to_n(l2))