class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right =None
def Insert(node,value):
    q=[]
    q.append(node)
    while len(q)!=0:
        current = q[0]
        if current.left:
            q.append(current.left)
        else:
            current.left = Node(value)
            break
        if current.right:
            q.append(current.right)
        else:
            current.right = Node(value)
            break
        q.pop(0)
def PreOrder(node):
    print(node.data)
    if node.left:
        PreOrder(node.left)
    if node.right:
        PreOrder(node.right)

def deleteFromTree(node,value):
    current = node
    while current.right:
        current =current.right
    #current is right most
    #print(current.data)
    #traverse in level order
    to_replace  =0
    to_node_delete = None
    if current.left:
        to_replace =current.left.data
        to_node_delete = current.left
    else:
        to_replace = current.data 
        to_node_delete = current   
    q=[]
    q.append(node)
    while(len(q)!=0):
        n=q[0]
        if n.data == value:
            n.data = to_replace   
        if n.left:
            q.append(n.left)
            if n.left is to_node_delete:
                n.left= None
                break
        if n.right:
            q.append(n.right)
            if n.right is to_node_delete:
                n.right = None
                break
                #q.append(n.ri)
        q.pop(0)

def LevelOrderTraversal(node):
    q=[]
    q.append(node)
    while(len(q)!=0):
        current = q[0]
        print(current.data)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        q.pop(0)      




tree = Node(3)
#arr = [2,4,6,8,10,15,14,13]
arr =[2,4,1,3,5]
for i in range(len(arr)):
    Insert(tree,arr[i])

#PreOrder(tree)
# deleteFromTree(tree,2)
# deleteFromTree(tree,12)
LevelOrderTraversal(tree)
           
