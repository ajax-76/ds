class Node:
    def __init__(self,value):
        self.data = value
        self.left =None
        self.right =None
class Convert:
    def __init__(self):
        self.arr =[]
    def ConstructBSTFromItsGivenLevelOrder(self,lvlarr,i):
        if i>len(lvlarr)-1:
            return None
        root =Node(lvlarr[i])
        root.left = self.ConstructBSTFromItsGivenLevelOrder(lvlarr,2*i+1)
        root.right = self.ConstructBSTFromItsGivenLevelOrder(lvlarr,2*i+2)
        return root
    def CreateBSTFromLvlOrder(self,node,value):
        q=[]
        q.append(node)
        while len(q)!=0:
            cur = q[0]
            if cur.left:
                q.append(cur.left)
            else:
                cur.left = Node(value)
                break
            if cur.right:
                q.append(cur.right)
            else:
                cur.right = Node(value)
                break   
            q.pop(0)
        return root
    def ConstructBST(self,root,value):
        if root is None:
            root =Node(value)
        if value<root.data:
            root.left = self.ConstructBST(root.left,value)
        if value>root.data:
            root.right = self.ConstructBST(root.right,value)
        return root
    def ConvertNormalBstToBalancedBst(self,arr):
        if len(arr) == 0:
            return None
        mid = int(len(arr)/2)
        root = Node(arr[mid])
        #print(arr[mid])
        root.left = self.ConvertNormalBstToBalancedBst(arr[:mid])
        root.right = self.ConvertNormalBstToBalancedBst(arr[mid+1:])
        return root
    def InorderSave(self,node):
        if node.left:
            self.InorderSave(node.left)
        self.arr.append(node.data)
        if node.right:
            self.InorderSave(node.right)
def InorderTraversal(root):
    if root.left:
        InorderTraversal(root.left)
    print(root.data)
    if root.right:
        InorderTraversal(root.right)
def PreOrder(root):
    print(root.data)
    if root.left:
        PreOrder(root.left)
    if root.right:
        PreOrder(root.right)
# arr = [7, 4, 12, 3, 6, 8, 1, 5, 10] 
# c=Convert()
# root = Node(arr[0])
# for i in range(1,len(arr)):
#     #print("print",arr[i])
#     root = c.ConstructBST(root,arr[i])
# root2 =c.ConstructBSTFromItsGivenLevelOrder(arr,0)
# InorderTraversal(root)
# print("-------------------") 
# InorderTraversal(root2)
            
root = Node(10) 
root.left = Node(8) 
root.left.left = Node(7) 
root.left.left.left = Node(6) 
root.left.left.left.left = Node(5)
c=Convert()
c.InorderSave(root)
print(c.arr)
arr1=c.arr
broot = c.ConvertNormalBstToBalancedBst(arr1)
PreOrder(broot)