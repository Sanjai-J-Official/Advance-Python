class Node:
   def __init__(self,val):
     self.val=val
     self.next=None 
     self.prev=None
    
lis=[10,20,30]

def insert_lis(lis):
  head=Node(lis[0])
  current=head
  for i in lis[1:]:
    current.next=Node(i)
    current.prev=current
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

def search_val(head,value):
   
  current=head 
  while current:
    if current.val==value :
      return True
    current=current.next
  return False 
def middle_val(head,count):
  # current=head
  # print("Count/2",count//2)
  # for i in range(count//2):
  #   current=current.next
  # return current.val 
  
  slow=fast=head 
  while fast and fast.next:
    slow=slow.next 
    fast=fast.next.next
  return slow.val 
  
head=insert_begin(head,value)
print_all(head)
count=find_length(head)
print(search_val(head,100))
print(middle_val(head,count))
 
