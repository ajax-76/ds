import sys
class Node:
    def __init__(self,value):
        self.data = value
        self.left =None
        self.right= None
class CheckNSearch:
    def __init__(self):
        self.preindex=0
        self.isbst = True
        self.stack = []
        self.parent = -sys.maxsize
        self.lca =None
        self.largetsBSTSize =0

    def CheckLevelOrderIsOfBST(self,lvlarr):
           q =[]
           q.append({
               "data":lvlarr[0],
               "min":-sys.maxint,
               "max":sys.maxint
           })
           n = len(lvlarr)
           i=1
           while len(q)!=0 and i!=n:
               temp =q.pop(0)
               if i<n and (lvlarr[i]<temp.data and lvlarr[i]>temp.min):
                   q.append({
                    "data":lvlarr[i],
                    "min":temp.min,
                    "max":temp.data
                   })
                   i=i+1
               if i<n and (lvlarr[i]<temp.data and lvlarr[i]<temp.max):
                    q.append({
                    "data":lvlarr[i],
                    "min":temp.data,
                    "max":temp.max
                    })
                    i=i+1
           if i==n:
                return True
           return False        
    def CheckGivenPreorderArrayisBST(self,prearr):
        s=[]
        isbst =True
        parent = -sys.maxsize
        for i in range(len(prearr)):
            if prearr[i]<parent:
                isbst =False
                break
            while len(s)!=0:
                laststackval = s[-1]
                if laststackval<prearr[i]:
                    parent = s.pop()
                else:
                    break    

            s.append(prearr[i])
        return isbst
    def CheckBinaryTReeisBSt(self,node):
        if node:
            if self.parent>node.data:
                self.isbst =False
                return
            while len(self.stack)!=0:
                l = self.stack[-1]
                if l<node.data:
                    self.parent = self.stack.pop()
                else:
                    break
            self.stack.append(node.data)
        if node.left:
            self.CheckBinaryTReeisBSt(node.left)
            self.CheckBinaryTReeisBSt(node.right)        
    def CheckBinaryTReeisBSTInorderStyle(self,node,prev):
        if node.left:
            self.CheckBinaryTReeisBSTInorderStyle(node.left,prev)
        if prev == None:
            prev = node.data
        else:
            if prev>node.data:
                self.isbst=False
        prev = node.data
        if node.right:
            self.CheckBinaryTReeisBSTInorderStyle(node.right,prev)        
    def LowestCommonAncestor(self,node,l1,l2):
        if node:
            if l1 < node.data and l2 >node.data:
                self.lca = node.data
            if l1<node.data and l2<node.data:
                self.LowestCommonAncestor(node.left,l1,l2)
            if l1>node.data and l2>node.data:
                self.LowestCommonAncestor(node.right,l1,l2)
            if node.data==l1:
                self.lca =l1
            else:
                self.LowestCommonAncestor(None,l1,l2)        
    def BSTMorisTRaversalKSmallest(self,node,k):
        arr=[]
        p = node
        while p is not None:
            if p.left:
                cur = p.left
                t = p.left
                #print("aya",cur.data)
                while cur.right:
                    cur = cur.right
                p.left =None
                cur.right = p
                p =t
            else:
                arr.append(p.data)
                p =p.right 
        print(arr[k-1])   
    def CheckDeadEndofBST(self,node,Min,Max):
        if node is None:
            return False,[]
        if Min== Max:
            return True,[node.data]
        t1,v1 = self.CheckDeadEndofBST(node.left,Min,node.data-1)
        t2,v2 = self.CheckDeadEndofBST(node.right,node.data-1,Max)
        t  = t1 or t2
        v=[]
        if t1 ==True:
            v.append(v1)
        if t2 ==True:
            v.append(v2)   
        return t,v
    def LargestNumberinBSTlessThanEqualToN(self,node,N):
        if node is None:
            return -1
        if node.data == N:
            return N    
        if N>node.data:
            k= self.LargestNumberinBSTlessThanEqualToN(node.right,N)
            if k==-1:
                return node.data
            else:
                return k    
        if N<node.data:
               return self.LargestNumberinBSTlessThanEqualToN(node.left,N)
    #def ShortestBetweenTwoNodes(self,node,n1,n2):
    def DistanceOfRootFromNode(self,node,n1,d):
        if node is None:
            return 0
        if node:
            if n1 == node.data:
                return d
            if n1<node.data:
                d=d+1
                d = self.DistanceOfRootFromNode(node.left,n1,d)
            if n1>node.data:
                d=d+1
                d = self.DistanceOfRootFromNode(node.right,n1,d)
        return d

    def LargestBSTSizeInBinaryTree(self,node):
        if node is None:
            return [],0
        d1,s1 = self.LargestBSTSizeInBinaryTree(node.left)
        d2,s2 = self.LargestBSTSizeInBinaryTree(node.right)
        print(d1,d2,s1,s2)
        if len(d1)==0 and len(d2) == 0:
            return [node.data],1
        if len(d1) !=0 and len(d2)!=0:
            if d1[0] < node.data and d2[0]>node.data:
                return [node.data],s1+s2+1
            else:
                
                if s1>s2:
                    return d1,s1
                if s1<s2:
                    return d2,s2
                else:
                   return [],0         
        else:
            print("45",d1)
            if len(d1)!=0:
                if node.data>d1[0]:
                    return [node.data],s1+1
                else:
                    return [],0    
            elif len(d2)!=0:
                if node.data<d2[0]:
                    return [node.data],s2+1
                else:
                    [],0        
    
    def LargestBSTSizeInBinaryTreev2(self,node):
        if node:
            #self.stack.append(node.data)
            if self.parent>node.data:
                self.largetsBSTSize = 0
                self.parent = self.stack[0]
            while len(self.stack)!=0:
                l = self.stack[-1]
                if l < node.data:
                    self.parent = self.stack.pop()
                    self.largetsBSTSize =self.largetsBSTSize+1
                else:
                    break
            self.stack.append(node.data)
            self.LargestBSTSizeInBinaryTreev2(node.left)
            self.LargestBSTSizeInBinaryTreev2(node.right)
    def RemoveBSTOutsideGivenRange(self,node,r1,r2):
        if node is None:
            return None
        node.left = self.RemoveBSTOutsideGivenRange(node.left,r1,r2)
        node.right = self.RemoveBSTOutsideGivenRange(node.right,r1,r2)
        if node.left is None and node.right is None:
            if node.data<r1 or node.data>r2:
                node =None
            return node
        if node.data<r1 or node.data>r2:
            #print("node",node.data,node.left,node.right)
            if node.left:
                node =node.left
            if node.right:
                node= node.right 
            else:
                node =node
            #print(node.data)
            return node
        else:
            return node             
    def addstackstoextremes(self,node,s,direction):
        if direction is 'left':
            cur = node
            while cur is not None:
                #print(cur.data,'left')
                s.append(cur)
                cur =cur.left
                
            return s
        else:
            cur = node
            while cur is not None:
                #print(cur.data,'right')
                s.append(cur)
                cur =cur.right  
            return s    

    def FindPairInGivenBst(self,node,target):
        s1 =[]
        s2= []
        if node:
            s1 = self.addstackstoextremes(node,s1,'left')
            s2 = self.addstackstoextremes(node,s2,'right')
            ret=False
            res = None,None
            while ret is False:
                if len(s1) !=0 and len(s2)!=0:
                    c1 = s1[-1].data
                    c2 = s2[-1].data
                    print(c1,c2)
                    if c1>c2:
                        ret =True
                        res=  0,0
                    if c1==c2:
                        ret =True
                        res=  0,0
                    if c1+c2 == target:
                        ret =True
                        return c1,c2    
                    if c1+c2 <target:
                        n = s1.pop()
                        if n.right:
                            s1 = self.addstackstoextremes(n.right,s1,'left')
                    if c1+c2>target:
                        n = s2.pop()
                        if n.left:
                            s2 = self.addstackstoextremes(n.left,s2,'right')
            return res                       
    
       



    

def insert(node,value):
    if node is None:
        return Node(value)
    if value<node.data:
       node.left = insert(node.left,value)
    if value>node.data:
       node.right = insert(node.right,value)                   
    return node
def InorderTraversal(root):
    if root.left:
        InorderTraversal(root.left)
    print(root.data)
    if root.right:
        InorderTraversal(root.right)           
pre1 = [40 , 30 , 35 , 20 ,  80 , 100] 

# root = Node(3)  
# root.left = Node(2)  
# root.right = Node(5)  
# root.right.left = Node(4)  
# root.right.right = Node(6)

# root = Node(20) 
# root.left = Node(8) 
# root.right = Node(22) 
# root.left.left = Node(4) 
# root.left.right = Node(12) 
# root.left.right.left = Node(10) 
# root.left.right.right = Node(14)

# root = None
# root = insert(root, 20)  
# insert(root, 10)  
# insert(root, 5)  
# insert(root, 15)  
# insert(root, 30)  
# insert(root, 25)  
# insert(root, 35)
# root = Node(50)  
# root.left     = Node(10)  
# root.right     = Node(60)  
# root.left.left = Node(5)  
# root.left.right = Node(20)  
# root.right.left = Node(55) 
# root.right.left.left = Node(45)  
# root.right.right = Node(70) 
# root.right.right.left = Node(65)  
# root.right.right.right = Node(80)
# root = Node(60)  
# root.left = Node(65)  
# root.right = Node(70)  
# root.left.left = Node(50)

# root = None
# root = insert(root, 6) 
# root = insert(root, -13)  
# root = insert(root, 14)  
# root = insert(root, -8)  
# root = insert(root, 15)  
# root = insert(root, 13)  
# root = insert(root, 7) 


root = Node(15); 
root.left = Node(10); 
root.right = Node(20); 
root.left.left = Node(8); 
root.left.right = Node(12); 
root.right.left = Node(16); 
root.right.right = Node(25);

c =CheckNSearch()
InorderTraversal(root)
#print(c.CheckGivenPreorderArrayisBST(pre1))
#c.CheckBinaryTReeisBSTInorderStyle(root,None)
#c.LowestCommonAncestor(root,4,10)
#print(c.lca)
#c.BSTMorisTRaversalKSmallest(root,2)
#print(c.LargestNumberinBSTlessThanEqualToN(root,6))
# d1=c.DistanceOfRootFromNode(root,5,0)
# d2=c.DistanceOfRootFromNode(root,35,0)
# c.LowestCommonAncestor(root,5,35)
# d3 = c.DistanceOfRootFromNode(root,c.lca,0)
print("-----------")
r2=c.FindPairInGivenBst(root,42)
print(r2)
#InorderTraversal(r2)
#print(c.stack,c.largetsBSTSize+len(c.stack))
