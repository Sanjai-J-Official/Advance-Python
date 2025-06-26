 class TreeNode:
  def __init__(self,val):
    self.key=val 
    self.left=None 
    self.right=None 
    

tuple_node=((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuble(data):
  if isinstance(data,tuple) and len(data)==3:
    node=TreeNode(data[1])
    node.left=parse_tuble(data[0])
    node.right=parse_tuble(data[2])
   
  elif data is None:
    node = None
  else:
    node=TreeNode(data)
  return node 
tree=parse_tuble(tuple_node)

def treeToTuble(root):
  if root is None:
    return None 
  if root.left is None and root.right is None:
    return root.key 
  return (treeToTuble(root.left),root.key,treeToTuble(root.right))
  
 
tup=treeToTuble(tree)
print(tup)
