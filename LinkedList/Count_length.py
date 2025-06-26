class Node:
   def __init__(self,val):
     self.val=val
     self.next=None 
    
lis=[10,20,30,40]

def insert_lis(lis):
  head=Node(lis[0])
  current=head
  for i in lis[1:]:
    current.next=Node(i)
    current=current.next
  return head 
  
  
head=insert_lis(lis)

def print_all(head):
  current=head
  while current:
    print(current.val, end="->")
    current=current.next
  print(None)
  
value=100

def insert_begin(head,value):
   current=Node(100)
   current.next=head 
   return current
   
def find_length(head):
  count=0 
  current=head
  while current:
    count+=1 
    current=current.next
  return count
head=insert_begin(head,value)  
print_all(head)
print("Count:",find_length(head))


