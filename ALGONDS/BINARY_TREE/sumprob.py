class Node:
    def __init__(self,value):
        self.data = value
        self.left=None
        self.right =None



class SumClass:
    def __init__(self):
        self.digonaldict={"0":0}
        self.sum = 0
    def DiagonalTraversalTree(self,node):
        q=[]
        q.append(node)
        curr = q[0]
        if curr.right:
            while curr.right:
                curr  =curr.right
                q.append(curr)
        while len(q)!=0:
            newcur = q[0]
            if newcur.left:
                q.append(newcur.left)
                temp  = newcur.left
                while temp.right is not None:
                    q.append(temp.right)
                    temp=temp.right
            print(newcur.data,end=" ")
            q.pop(0)
    def DiagonalSumTree(self,node,level):
        try:
            self.digonaldict[str(level)] = self.digonaldict[str(level)]+node.data
        except:
            self.digonaldict[str(level)] = node.data
        if node.right:
            self.DiagonalSumTree(node.right,level)
        if node.left:
            self.DiagonalSumTree(node.left,level+1)    
    def LeafPathSum(self,node):
        if node.left:
            self.LeafPathSum(node.left)
        if node.right:
            self.LeafPathSum(node.right)
        if node.left and node.right:
            print(node.left.data+node.right.data)
    def SumofNodeOfLongestPathRootToLeaf(self,node,s):
        if node is None:
            return 0,0
        l1,s1 = self.SumofNodeOfLongestPathRootToLeaf(node.left,s)
        l2,s2= self.SumofNodeOfLongestPathRootToLeaf(node.right,s)
        if l1>=l2:
            return 1+l1,node.data+s1
        if l2>l1:
            return 1+l2,node.data+s2          
    def RemoveAllNodesDontLieInAnyPath(self,node,s,k):
        if node is None:
            return 0,None
        if node.left or node.right:
            s=s+node.data
        c1,node.left = self.RemoveAllNodesDontLieInAnyPath(node.left,s,k)
        c2,node.right = self.RemoveAllNodesDontLieInAnyPath(node.right,s,k)
        if node.left is None and node.right is None:
            c = s+node.data
            if c <k:
                return s,None
        return s,node
    def InorderTraversal(self,node):
        if node.left:
            self.InorderTraversal(node.left)
        if node:
            print(node.data)    
        if node.right:
            self.InorderTraversal(node.right)
    def MaximumPathSumBetweenTwoLeaves(self,node):
        if node is None:
            return 0
        lval = self.MaximumPathSumBetweenTwoLeaves(node.left)
        rval =self.MaximumPathSumBetweenTwoLeaves(node.right)
        if lval+rval +node.data>self.sum:
            self.sum = lval+rval +node.data
        return max(lval,rval)+node.data    
    def MaximumPathSumRootToLeafPath(self,node):
        if node is None:
            return 0
        lval = self.MaximumPathSumBetweenTwoLeaves(node.left)
        rval =self.MaximumPathSumBetweenTwoLeaves(node.right)
        return max(lval,rval)+node.data



# root= Node(1)
# root.left =  Node(2)
# root.right =  Node(3) 
# root.left.left =  Node(9) 
# root.left.right =  Node(6) 
# root.right.left =  Node(4) 
# root.right.right =  Node(5) 
# root.right.left.right =  Node(7) 
# root.right.left.left =  Node(12) 
# root.left.right.left =  Node(11) 
# root.left.left.right =  Node(10) 

# root =  Node(8)  
# root.left =  Node(5)  
# root.right =  Node(4)  
# root.left.left =  Node(9)  
# root.left.right =  Node(7)  
# root.left.right.left =  Node(1)  
# root.left.right.right =  Node(12)  
# root.left.right.right.right =  Node(2) 
# root.left.right.right.left =  Node(6)  
# root.right.right =  Node(11)  
# root.right.right.left =  Node(3) 

# root =  Node(4)         #     4      
# root.left =  Node(2)         #     / \      
# root.right =  Node(5)     #     2 5      
# root.left.left =  Node(7) #     / \ / \      
# root.left.right =  Node(1) # 7 1 2 3  
# root.right.left =  Node(2) #     /          
# root.right.right =  Node(3) #     6          
# root.left.right.left =  Node(6)



# root = Node(5)
# root.right=Node(3)
# root.right.left=Node(10)
# root.right.right=Node(10)
# root.left=Node(2)
# root.left.left= Node(1)
# root.left.right=Node(4)
# root.left.right.left=Node(6)
# root.left.right.right=Node(8)

# root = Node(1)  
# root.left = Node(2)  
# root.right = Node(3)  
# root.left.left = Node(4)  
# root.left.right = Node(5)  
# root.right.left = Node(6)  
# root.right.right = Node(7)  
# root.left.left.left = Node(8)  
# root.left.left.right = Node(9)  
# root.left.right.left = Node(12)  
# root.right.right.left = Node(10)  
# root.right.right.left.right = Node(11)  
# root.left.left.right.left = Node(13)  
# root.left.left.right.right = Node(14)  
# root.left.left.right.right.left = Node(15)


# root = Node(-15) 
# root.left = Node(5) 
# root.right = Node(6) 
# root.left.left = Node(-8) 
# root.left.right = Node(1) 
# root.left.left.left = Node(2) 
# root.left.left.right = Node(6) 
# root.right.left = Node(3) 
# root.right.right = Node(9) 
# root.right.right.right= Node(0) 
# root.right.right.right.left = Node(4) 
# root.right.right.right.right = Node(-1) 
# root.right.right.right.right.left = Node(10) 
root = Node(10)
root.left = Node(-2) 
root.right = Node(7)
root.right.right = Node(7) 
root.left.left = Node(8) 
root.left.right = Node(-4)

sumc = SumClass()
# sumc.InorderTraversal(root)
# print("------------------------------")
# s , newroot=sumc.RemoveAllNodesDontLieInAnyPath(root,0,45)
# print("------------------------------")
# sumc.InorderTraversal(newroot)

#sumc.LeafPathSum(root)
#print(sumc.SumofNodeOfLongestPathRootToLeaf(root,0))

print(sumc.MaximumPathSumRootToLeafPath(root),sumc.sum)