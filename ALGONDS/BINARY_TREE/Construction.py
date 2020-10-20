class Node:
    def __init__(self,value):
        self.data = value
        self.left=None
        self.right=None
        self.preindex = 0
        self.index =0

class NaryLeftChildRightChildNode:
    def __init__(self,value):
        self.data = value
        self.child = None
        self.Next =None


class ConvertClass:
    def __init__(self):
        self.preindex = 0
        self.index =0
    def ConvertTreeFromPreNInArr(self,inarr,prearr,indict,start_index,last_index):
        if start_index>last_index:
            return None
        currval = prearr[self.preindex] # root node for first call
        self.preindex =self.preindex+1
        cnode = Node(currval)
        if start_index == last_index:
            return cnode
        inindex = indict[currval]
        cnode.left = self.ConvertTreeFromPreNInArr(inarr,prearr,indict,start_index,inindex-1)
        cnode.right = self.ConvertTreeFromPreNInArr(inarr,prearr,indict,inindex+1,last_index)
        return cnode
    def ConvertTreeFromLevelNInArr(self,lvarr,inarr):
        if len(lvarr) is 0:
            return None
        rootval = lvarr[0]
        root = Node(rootval)
        mid = inarr.index(rootval)
        leftarr  =  [inarr[i] for i in range(0,mid)]
        rightarr =  [inarr[i] for i in range(mid+1,len(inarr))]
        leftrarrange =[]
        rightarrange =[]
        for i in range(len(lvarr)):
            if lvarr[i] in leftarr:
                leftrarrange.append(lvarr[i])
        for i in range(len(lvarr)):
            if lvarr[i] in rightarr:
                rightarrange.append(lvarr[i])
        #print("lvl",leftrarrange)        
        root.left = self.ConvertTreeFromLevelNInArr(leftrarrange,inarr)
        root.right = self.ConvertTreeFromLevelNInArr(rightarrange,inarr)
        return root           
    def ConstructTreeWithPreNPost(self,prearr,postarr):
        
        rootval = prearr[self.preindex]
        #print("preindex",self.preindex,postarr , rootval)
        root = Node(rootval)
        self.preindex =self.preindex+1    
        if len(postarr)==1:
            return root
        
        postindex = postarr.index(prearr[self.preindex])
        leftpostarr = [postarr[i] for i in range(0,postindex+1)]
        rightpostarr = [postarr[i] for i in range(postindex+1,len(postarr)-1)]
        #print(leftpostarr,rightpostarr)
        root.left =  self.ConstructTreeWithPreNPost(prearr,leftpostarr)
        root.right = self.ConstructTreeWithPreNPost(prearr,rightpostarr)
        return root
    def ConstructTreeFromPreNMirrorPre(self,prearr,mirprearr):
        curval = prearr[self.preindex]
        self.preindex =self.preindex+1
        root = Node(curval)
        #print("mir",mirprearr)
        if len(mirprearr)==1:
            return root
        midindex = mirprearr.index(prearr[self.preindex])
        leftmirarr =  [mirprearr[i] for i in range(midindex,len(mirprearr))]
        rightmirarr = [mirprearr[i] for i in range(1,midindex)]
        #print(leftmirarr,rightmirarr)
        root.left = self.ConstructTreeFromPreNMirrorPre(prearr,leftmirarr)
        root.right = self.ConstructTreeFromPreNMirrorPre(prearr,rightmirarr)
        return root
    def ConstructSpecialTreeGivenPreOrder(self,prearr,preLNarr):
        curval = prearr[self.preindex]
        root = Node(curval)
        checkNOrL = preLNarr[self.preindex]
        self.preindex = self.preindex+1
        if checkNOrL is 'L':
            return root
        root.left = self.ConstructSpecialTreeGivenPreOrder(prearr,preLNarr)
        root.right =self.ConstructSpecialTreeGivenPreOrder(prearr,preLNarr)
        return root
    def ConstructSpecialTreeFromInorder(self,inarr):
        if len(inarr) == 0:
            return None 
        maxval = max(inarr)
        indexofMax= inarr.index(maxval)
        root = Node(maxval)
        if len(inarr) == 1:
            return root
        leftsubarray = [inarr[i] for i in range(0,indexofMax)]
        rightsubarray = [inarr[i] for i in range(indexofMax+1,len(inarr))]
        root.left =self.ConstructSpecialTreeFromInorder(leftsubarray)
        root.right = self.ConstructSpecialTreeFromInorder(rightsubarray)
        return root
    def ConstructWithBracketRepresentation(self,bracketarray):
        if self.index > len(bracketarray)-1:
            return None
        if bracketarray[self.index]=='(':
            self.index =self.index+1
        if bracketarray[self.index]==')':
            self.index=self.index+1
            return None
        val = bracketarray[self.index]
        self.index=self.index+1
        root = Node(val)
        #print(val,self.index)
        root.left =self.ConstructWithBracketRepresentation(bracketarray)
        root.right =self.ConstructWithBracketRepresentation(bracketarray)
        return root
    def ConstructTreeChildrenSumProperty(self,node):
        root =node
        if node.left:
            self.ConstructTreeChildrenSumProperty(node.left)
        if node.right:
            self.ConstructTreeChildrenSumProperty(node.right)
        if root.left and root.right:
            leftval = root.left.data
            rightval = root.right.data
            if leftval+rightval>root.data:
                root.data =leftval+rightval
            if leftval+rightval<root.data:
                diff = root.data-(leftval+rightval)
                root.left.data = root.left.data+diff
        if node.left and not node.right:
            root.left.data=root.data
        if node.right and not node.left:
            root.right.data=root.data    
    def LeftRightRepresentationOfBinaryTree(self,node):
        if node is None:
            return None    
        lrnode = NaryLeftChildRightChildNode(node.data)
        if node.left:
            lrnode.child=self.LeftRightRepresentationOfBinaryTree(node.left)
        if node.right:
            lrnode.child.Next=self.LeftRightRepresentationOfBinaryTree(node.right)
        return lrnode
    def BinaryTreeIntoMirrorTree(self,node):
        if node is None:
            return None
        mirrornode =Node(node.data)
        if node.right:
            mirrornode.left = self.BinaryTreeIntoMirrorTree(node.right)
        if node.left:
            mirrornode.right=self.BinaryTreeIntoMirrorTree(node.left)
        return mirrornode    
        
def Insert(root,value):
    q=[]
    q.append(root)
    while len(q) is not 0:
        curr = q[0]
        if curr.left:
            q.append(curr.left)
        else:
            curr.left= Node(value)
            break
        if curr.right:
            q.append(curr.right)
        else:
            curr.right = Node(value)
            break
        q.pop(0)





def PreOrderTraversal(node):
    print(node.data)
    if node.left:
        PreOrderTraversal(node.left)
    if node.right:
        PreOrderTraversal(node.right)    
def PostOrderTraversal(node):
    if node.left:
        PostOrderTraversal(node.left)
    if node.right:
        PostOrderTraversal(node.right)
    print(node.data)
def InorderTraversal(node):
    if node.left:
        InorderTraversal(node.left)
    print(node.data)
    if node.right:
        InorderTraversal(node.right)
def LeftRightTraversal(node):
    print(node.data)
    if node.Next:
        LeftRightTraversal(node.Next)
    if node.child:
        LeftRightTraversal(node.child)    

inarr= ['D', 'B', 'E', 'A', 'F', 'C' ]
prearr = ['A', 'B', 'D', 'E', 'C', 'F' ]

inarr1 = [4,8,10,12,14,20,22]
lvlarr = [20,8,22,4,12,10,14]

prearr1 = [1,2,4,8,9,5,3,6,7]
postarr1 =[8,9,4,5,2,6,7,3,1]

prearr2= [1,2,4,5,3,6,7]
mirarr1= [1,3,7,6,2,5,4]

prearr3=[10, 30, 20, 5, 15]
preLNarr=['N', 'N', 'L', 'L', 'L']

inarr2 = [1,5,10,40,30,15,28,20]
dictin = {val:inx for inx,val in enumerate(inarr)}

c = ConvertClass()
#tree = c.ConvertTreeFromPreNInArr(inarr,prearr,dictin,0,len(inarr)-1)
#tree = c.ConvertTreeFromLevelNInArr(lvlarr,inarr1)
#tree = c.ConstructTreeWithPreNPost(prearr1,postarr1)
#tree = c.ConstructTreeFromPreNMirrorPre(prearr2,mirarr1)
#tree= c.ConstructSpecialTreeGivenPreOrder(prearr3,preLNarr)
#tree =c.ConstructSpecialTreeFromInorder(inarr2)
#tree =c.ConstructWithBracketRepresentation('4(2(3)(1))(6(5))')
#PreOrderTraversal(tree)

# root = Node(50) 
# root.left     = Node(7) 
# root.right     = Node(2) 
# root.left.left = Node(3) 
# root.left.right = Node(5) 
# root.right.left = Node(1) 
# root.right.right = Node(30)
# InorderTraversal(root)
# c.ConstructTreeChildrenSumProperty(root)
# c.ConstructTreeChildrenSumProperty(root)
# print("---------------------")
# InorderTraversal(root)

# root = Node(1) 
# root.left = Node(2)
# root.left.left=Node(8)
# root.left.right=Node(7) 
# root.right = Node(3) 
# root.right.left = Node(4) 
# root.right.right = Node(5) 
# root.right.left.left = Node(6) 
# root.right.right.left = Node(7) 
# root.right.right.right = Node(8)
root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)
#tree =c.LeftRightRepresentationOfBinaryTree(root)
tree = c.BinaryTreeIntoMirrorTree(root)
InorderTraversal(tree)