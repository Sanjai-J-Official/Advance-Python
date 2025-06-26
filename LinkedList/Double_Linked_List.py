class Node:
   def __init__(self,val):
     self.val=val
     self.next=None 
     self.prev=None
    
n1=Node(10)

n2=Node(20)
n1.next=n2 
n2.prev=n1 

n3=Node(30)
n3.prev=n2
n2.next=n3

head=n1  
def print_all(head):
  current=head
  while current:
    print(current.val, end="->")
    
    current=current.next
  print(None) 
print_all(head)
print(n3.prev.val) 
 
 
