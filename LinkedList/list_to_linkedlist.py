lis=[10,20,30,40]
class Node:
    def __init__(self,val):
        self.val=val 
        self.next=None 
  
def Solution(lst):
  if not lst:
    return None
  head=Node(10)
  current=head
  for value in lis[1:]:
    current.next=Node(value)
    current=current.next 
  return head 

def print_all(head):
  current=head 
  while current:
    print(current.val , end="->")
    current=current.next 
    
print(print_all(Solution(lis)))
