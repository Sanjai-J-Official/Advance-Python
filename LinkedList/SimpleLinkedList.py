 class Node:
  def __init__(self,val):
    self.val=val
    self.next=None 
head=None    
def insert_node(head,value):
  new_node=Node(value)
  if not head:
    return new_node
  current=head
  while current.next:
    current=current.next 
  current.next=new_node 
  return head 

lis=[10,20,30]
for i in lis:
  head=insert_node(head,i)

count=0
current=head
while current:
  print(current.val,end="->")
  current=current.next
  count+=1 
print("\nCount",count)
  
def search_node(head,value):
  current=head
  while current:
    if current.val==value:
      return True 
    current=current.next 
  return False
  
print(search_node(head,20))
 

  
