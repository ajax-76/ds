class Node:
    def __init__(self,value):
        self.data = value
        self.left= None
        self.right =None
def Insert(node,value):
    q =[]
    q.append(node)
    while len(q)!=0:
        n = q[0]
        if n.left:
            q.append(n.left)
        else:
            n.left = Node(value)
            break
        if n.right:
            q.append(n.right)
        else:
            n.right = Node(value)
            break
        q.pop(0) 
def LevelOrderTraversal(node):
    q1 =[]
    q1.append(node)
    while len(q1)!=0:
        n = q1[0]
        print(n.data)
        if n.left:
            q1.append(n.left)
        if n.right:
            q1.append(n.right)
        q1.pop(0)

def CheckBTreeIsContinous(node):
    #do a level order traversal
    q=[]
    e=[]
    q.append(node)
    while(len(q)!=0):
        n  = q[0]
        temp_root_data = n.data
        if n.left:
            q.append(n.left)
            d=abs(temp_root_data - n.left.data)
            if d !=1:
                e.append({"path":str(temp_root_data)+"->"+str(n.left.data)})
        if n.right:
            q.append(n.right)
            d=abs(temp_root_data - n.right.data)
            if d !=1:
                e.append({"path":str(temp_root_data)+"->"+str(n.right.data)})
        q.pop(0)
    return e    

tree =  Node(3)
#arr = [2,4,1,3,5]
arr= [5,8,6,4,10]
for i in range(len(arr)):
    Insert(tree,arr[i])
LevelOrderTraversal(tree)
error = CheckBTreeIsContinous(tree)
print(error)