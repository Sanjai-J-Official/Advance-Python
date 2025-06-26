class Node:
   def __init__(self,val):
     self.val=val
     self.next=None 
     self.prev=None
    


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
 
def remove_duplicate(head):
  current=head 
  li=[]
  prev=None
  while current:
    
    if current.val not in li:
      prev=current
      li.append(current.val) 
    else:
      prev.next=current.next
       
      
     
    current=current.next
  return head
  
lis=[10,20,10,30,20,40]   
head=insert_lis(lis)
print_all(head)
#head=reverse_list(head)
head=remove_duplicate(head)
print_all(head)

 
 
 
