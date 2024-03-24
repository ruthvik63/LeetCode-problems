class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def palindrome(head):
    #middle element of linked list
    slow=fast=head

    while fast or fast.next:
        slow=slow.next
        fast=fast.next
    #reversing the linked list
    prev=None
    while slow:
        next_node=slow.next
        slow.next=prev
        prev=slow
        slow=next_node
    #comparing the linked list
    
    while prev:
        if head.val!=prev.val:
            return False
        head=head.next
        prev=prev.next
    return True