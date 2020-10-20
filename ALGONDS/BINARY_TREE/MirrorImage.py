class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right =None
 #check total right in right sub tree equal in left sub tree
class MirrorImage:
    def __init__(self):
        self.count_left = 0
        self.count_right = 0   
    def CheckMirror_image_2(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1.data == node2.data:
            return self.CheckMirror_image_2(node1.left,node2.right) and self.CheckMirror_image_2(node1.right,node2.left)
        if node1.data!=node2.data:
            return False
        else:
            return True
    def CheckifFoldable(self,node):
        pass        
    def CheckifFoldableIterative(self,node):
        q1=[]
        q2 =[]
        q1.append(node.left)
        q2.append(node.right)
        while len(q1)!=0 and len(q2)!=0:
            n1=q1[0]
            n2=q2[0]
            if n1 and n2:
                return False
            if n1.left:
                q1.append(n1.left)
            if n1.right:
                q1.append(n1.right)
            if n2.right:
                q2.append(n2.right)
            if n2.left:
                q2.append(n2.left)
            q1.pop(0)
            q2.pop(0)
        return True        

    def CheckMirror_Iterative(self,node):
        q1=[]
        q2 =[]
        q1.append(node.left)
        q2.append(node.right)
        while len(q1)!=0 and len(q2)!=0:
            n1=q1[0]
            n2=q2[0]
            if n1 and n2:
                if  n1.data !=n2.data:
                    return False
            if n1.left:
                q1.append(n1.left)
            if n1.right:
                q1.append(n1.right)
            if n2.right:
                q2.append(n2.right)
            if n2.left:
                q2.append(n2.left)
            q1.pop(0)
            q2.pop(0)
        return True                                      


def Insert(node,value):
    q=[]
    q.append(node)
    while(len(q)!=0):
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

# tree = Node(10)
# #arr = [2,4,6,8,10,15,14,13]
# arr =[7,15,9,11]
# for i in range(len(arr)):
#     Insert(tree,arr[i])
# LevelOrderTraversal(tree)
mirror = MirrorImage()

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 
#print(mirror.CheckMirror_image_2(root,root))
print(mirror.CheckMirror_Iterative(root))
#print("count left - right",mirror.count_left,mirror.count_right)
