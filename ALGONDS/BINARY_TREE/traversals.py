class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right =None
        self.Next= None

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
def InorderTraversalWthoutRecursion(node):
    s = []
    s.append(node)
    current = node
    #print("firstprint",current.left.right.left.data)
    while len(s)!=0:
        if current.left:
            current = current.left
            s.append(current)
        elif not current.left and current.right:
            print(current.data)
            s.pop()
            current = current.right
            s.append(current)
        if current.left is None and current.right is None:
            print(current.data)
            s.pop()
            if len(s)>0:
                current = s[len(s)-1]
                current.left =None

def MorrisTraversalInorder(node):
    current =node
    #print(current.data)
    while current is not None:
        if current.left is None:
            print(current.data)
            current =current.right
        else:
            pred = current.left
            temp =current.left
            while pred.right is not None:
                pred =pred.right
                #print("pred right ",pred.right.data)
            if pred.right is None:    
                #print("pred",pred.data)
                pred.right = current
                current.left=None
                current = temp
                #print("cur",current.data,current.right.data)   

#elegant
def MorrisPreOrderTraversal(node):
    current = node
    while current:
        if current.left:
            print(current.data)
            temp = current.left
            while temp.right:
                temp =temp.right
            temp.right = current.right
            current = current.left
        else:
            print(current.data)
            current=current.right
def ReverseTreePath_2(node,val,que):  
    if node is None:
        #que.pop()
        return []
    if node.data == val:
        que.append(node.data)
        #print(que[0],"--!!")
        node.data = que[0]
        que.pop(0)
        return que
    que.append(node.data)
    #print(que,"front")
    leftque = ReverseTreePath_2(node.left,val,que)
    rightque = ReverseTreePath_2(node.right,val,que)
    if len(leftque) is not 0:
        node.data = leftque[0]
        leftque.pop(0)
        return leftque
    if len(rightque) is not 0:
        node.data = rightque[0]
        rightque.pop(0)
        return rightque
    que.pop()    
    return []
class PReddSucSum:
    def __init__(self):
        self.summarr=[]
        self.index= 0
        self.next_p = None
        self.root = None
        self.rootData = None
    def ReverseTreePath(self,node,val):
        if self.rootData is None:
            self.rootData=node.data
        # inordertraversal
        if node.left:
            self.ReverseTreePath(node.left,val)
        if node.data ==val:
            node.data = self.rootData
        elif node.data == self.rootData:
           node.data = val
        print(node.data)
        if node.right:
            self.ReverseTreePath(node.right,val)
               
                
    def TreeSpecificTraversal(self,node):
        q1 =[]
        q2=[]
        q1.append(node)
        q2.append(node)
        out=[]
        while len(q1)!=0 and len(q2)!=0:
            curr1 = q1[0]
            curr2=q2[0]
            #print("curr", curr1.data,curr2.data)
            if q1[0]==q2[0]:
                out.append(curr1.data)
                if curr1.left:
                    q1.append(curr1.left)
                    out.append(curr1.left.data)
                if curr1.right:
                    q2.append(curr1.right)
                    out.append(curr1.right.data)
                q1.pop(0)
                q2.pop(0)
            else:
                #print("diagnose",out)
                if curr1.left:
                    q1.append(curr1.left)
                    out.append(curr1.left.data)
                if curr2.right:
                    q2.append(curr2.right)
                    out.append(curr2.right.data)
                if curr1.right:
                    q1.append(curr1.right)
                    out.append(curr1.right.data)
                if curr2.left:
                    q2.append(curr2.left)
                    out.append(curr2.left.data)
                q1.pop(0)
                q2.pop(0)
        # print(out)
        while len(out)!=0:
            print(out.pop(0),end=" , ")  

    def DiagonalTraversal(self,node):
        q=[]
        q.append(node)
        curr = q[0]
        if curr.right:
            while curr.right:
                curr  =curr.right
                q.append(curr)
        while len(q) is not 0:
            newcurr = q[0]
            if newcurr.left:
                q.append(newcurr.left)
                leftcur = newcurr.left
                while leftcur.right is not None:
                    leftcur =leftcur.right
                    q.append(leftcur)
            print(newcurr.data,end="  ")
            q.pop(0)
    def BoundaryTraversal(self,node):
        q=[]
        s=[]
        #q.append(node)
        print("root",node.data)
        current = node
        if current.left:
            while current.left is None:
                current = current.left
                q.append(current)
                newcurleft = current
                #if newcurleft.left:



    def CalSumInOrderPredecessorAndInorderSuccesor(self,node):
        #make inorder Traversal
        if node.left:
            self.CalSumInOrderPredecessorAndInorderSuccesor(node.left)
        self.summarr.append(node.data)
        #print(node.data,self.index)
        if node.right:
            self.CalSumInOrderPredecessorAndInorderSuccesor(node.right)
        #print(summarr)  
    def MakeSumInOrderPredecessorAndInorderSuccesor(self,node):
        if node.left:
            self.MakeSumInOrderPredecessorAndInorderSuccesor(node.left)
        if self.index ==0:
            node.data = self.summarr[self.index+1]
        elif self.index == len(self.summarr)-1:
            node.data = self.summarr[self.index-1]
        else:
            node.data = self.summarr[self.index-1]+self.summarr[self.index+1]
        self.index =self.index+1    
        if node.right:
            self.MakeSumInOrderPredecessorAndInorderSuccesor(node.right)
    def InorderTv(self,node):
        Next=None
        if node.right:
            self.InorderTv(node.right)
        print("node",node.data)
        node.next = Next
        Next =node
        if node.right:
            self.InorderTv(node.right)
    def PrintInorderSucessor(self,node,value):
        if node.right:
            self.PrintInorderSucessor(node.right,value)
        if node.data== value:
            print("aya",node.data)
            if self.next_p:
                print(self.next_p.data)
            else:
                print(0)
        self.next_p = node        
        if node.right:
            self.PrintInorderSucessor(node.left,value)
    def PrintnthNodeinoerder(self,node,val):
        if node.left:
            self.PrintnthNodeinoerder(node.left,val)
        self.index = self.index+1
        if self.index==val:
            print(node.data)
        if node.right:
            self.PrintnthNodeinoerder(node.right,val)
    def DensityBinaryTree(self,node):
        if node is None:
            return -1 , 1
        left , c1 = self.DensityBinaryTree(node.left)
        right ,c2 = self.DensityBinaryTree(node.right)
        return max(left,right)+1,c1+c2
    def Count_Binary_Trees(self,n):
        #DP Problem
        T=[0]*(n+1)
        T[0]=T[1] =1
        for i in range(2,n+1):
            for j in range(i):
                T[i] = T[i]+T[j] + T[i-j-1]
        return T[n]        

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
def LevelOrderSpiralTraversal(node):
    q1=[]
    q2=[]
    q1.append(node)
    while(len(q1)!=0) or len(q2) is not 0:
        #print("aya2")
        while len(q1) is not 0:
            current1 = q1[-1]
            print(current1.data)
            q1.pop()
            if current1.right:
                q2.append(current1.right)
            if current1.left:
                q2.append(current1.left)
            #q1.pop(0)    
        while len(q2) is not 0:
            current2 =q2[-1]
            print(current2.data)
            q2.pop()
            if current2.left:
                q1.append(current2.left)
            if current2.right:
                q1.append(current2.right)
            #q2.pop(0)

def TwoLevelorderTraversalWithDirectionChange(node):
    q1 =[]
    q2 =[]
    q3 =[]
    q4 =[]
    q1.append(node)
    while len(q1) is not 0 or len(q2) is not 0 or len(q3) is not 0 or len(q4) is not 0:
        while len(q1) is not 0:
            curr = q1[0]
            print(curr.data)
            if curr.left:
                q2.append(curr.left)
            if curr.right:
                q2.append(curr.right)
            q1.pop(0)    
        while len(q2) is not 0:
            curr = q2[0]
            print(curr.data)
            if curr.left:
                q3.append(curr.left)
            if curr.right:
                q3.append(curr.right)
            q2.pop(0)
        while len(q3) is not 0:
            curr = q3[-1]
            print(curr.data)
            if curr.right:
                q4.append(curr.right)
            if curr.left:
                q4.append(curr.left)
            q3.pop()
        while len(q4) is not 0:
            curr = q4[0]
            print(curr.data)

def ReverseLevelOrderTraversal(node):
    q =[]
    s=[]
    q.append(node)
    while len(q) is not 0:
        curr = q[0]
        s.append(str(curr.data))
        if curr.right:
            q.append(curr.right)
        if curr.left:
            q.append(curr.left)
        q.pop(0)    
    while len(s) is not 0:
        p = s.pop()
        print(p,end=" ")        
def InorderTraversal(root):
    if root.left:
        InorderTraversal(root.left)
    print(root.data)
    if root.right:
        InorderTraversal(root.right)

    


# tree = Node(12)
# #arr = [2,4,6,8,10,15,14,13]
# arr =[2,4,6,8,10,15,14,13,18,20]
tree=Node(1)
arr=[2,3,4,5,6,7,8]
for i in range(len(arr)):
    Insert(tree,arr[i])


root = Node(8) 
root.left = Node(3) 
root.right = Node(10) 
root.left.left = Node(1) 
root.left.right = Node(6) 
root.right.right = Node(14) 
root.right.right.left = Node(13) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 

#LevelOrderTraversal(tree)
print("------------------")
#InorderTraversalWthoutRecursion(tree)
print("------------------")
v =PReddSucSum()
# v.CalSumInOrderPredecessorAndInorderSuccesor(tree)
# v.MakeSumInOrderPredecessorAndInorderSuccesor(tree)
#LevelOrderTraversal(tree)
#v.InorderTv(tree)
#v.PrintInorderSucessor(tree,5)
#InorderTraversalWthoutRecursion(root)
InorderTraversal(root)
print("------------------")
ReverseTreePath_2(root,4,[])
InorderTraversal(root)
#InorderTraversalWthoutRecursion(root)
#v.DiagonalTraversal(tree)
#v.PrintnthNodeinoerder(tree,6)
print("------------------")
#ReverseLevelOrderTraversal(tree)
print("------------------")
#c, c1 = v.DensityBinaryTree(tree)
#print(c,c1)
#LevelOrderSpiralTraversal(tree)