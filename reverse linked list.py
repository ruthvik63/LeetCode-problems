class Node:
    def __init__(self,val,head=None):
        self.val=val
        self.head=head



def reverse(head:Node):
    prev=None
    temp=head

    while temp!=None:
        next_node=temp.head
        temp.next=prev
        prev=temp
        temp=next_node
    return prev

node1=Node(5)
node2=Node(6)
node3=Node(7)
node1.next=node2
node2.next=node3

a=reverse(node1)
print(a.val)

#recursive method----------------------


# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head==None or head.next==None:
#             return head
#         else:
#             new_node=self.reverseList(head.next)
#             front=head.next
#             front.next=head
#             head.next=None
#             return new_node