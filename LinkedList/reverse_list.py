class Node:
   def __init__(self,val):
     self.val=val
     self.next=None 
     self.prev=None
    

lis=[10,20,30,40] 
def insert_lis(lis):
  head=Node(lis[0])
  current=head
   
  
  for i in lis[1:]:
    current.next=Node(i)
    current=current.next
   
  return head 

def print_all(head):
  current=head
  while current:
    print(current.val, end="->")
    
    current=current.next
  print(None) 
def reverse_list(head):
  current=head 
  prev=None 
  while current: #10 20
    next_node=current.next  #20
    
    current.next=prev  #10
     
    prev=current #10 20
    current=next_node 
  return prev 
  
  
head=insert_lis(lis)
head=reverse_list(head)
print_all(head)

 
 
 
