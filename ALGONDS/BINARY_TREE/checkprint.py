class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class CheckClass:
    def __init__(self):
        self.check =True
        self.checkifBTiseinhalf=False
        self.preindex =0
        self.checkforRootval = False
        self.issubtree=True
        self.keepverticalarrayR =[]
        self.keepverticalarrayL=[]
    def CheckForChildrenSumProperty(self,node):
        if node.left:
            self.CheckForChildrenSumProperty(node.left)
        if node.right:
            self.CheckForChildrenSumProperty(node.right)
        if node.right and node.left:
            if node.data!=node.right.data+node.left.data:
                self.check=False
        if node.left and not node.right:
            if node.data!=node.left.data:
              self.check=False
        if node.right and not node.left:
            if node.data is not node.right.data:
                self.check =False      
    def CheckBinarySumTree(self,node):
        #print("aya")
        if node is None:
            return 0,True
        s1,bl1=self.CheckBinarySumTree(node.left)
        s2,bl2=self.CheckBinarySumTree(node.right)
        #print("nde ",node.data,s1,s2)
        if s1 is 0 and s2 is 0:
            #self.check=True
            return node.data,True
        if node.left is None and node.right is None:
            return node.data,True
        total_sum =s1+s2
        #print(total_sum,s1,s2)
        if total_sum!=node.data:
            # self.check=False
            return total_sum+node.data,False
        else:
            return total_sum+node.data,True
        # print(total_sum+node.data)    
        # return total_sum+node.data   
    def CheckSumCoverdNUncovered(self,node):
        q1=[]
        q2=[]
        q3 =[]
        sum1=0
        sum2=0
        q1.append(node)
        while len(q1) is not 0 or len(q2) is not 0 or len(q3) is not 0:
            current1=None
            current2=None
            if len(q1) is not 0:
                current1 = q1[0]
            if current1 is node:
                if current1.left:
                    q1.append(current1.left)
                    #sum1=sum1+current1.left.data
                if current1.right:
                    q2.append(current1.right)
                    #sum1=sum1+current1.right.data
                sum1=sum1+q1.pop(0).data
            else:
                if len(q2) is not 0:
                  current2 = q2[0]
                if current1:
                    if current1.left:
                        q1.append(current1.left)
                        #sum1=sum1+current1.left.data
                    if current1.right:
                        q3.append(current1.right)
                if current2:
                    if current2.right:
                        q2.append(current2.right)
                        #sum1=sum1+current2.right.data
                    if current2.left:
                        q3.append(current2.left)
                if len(q1) is not 0:
                    sum1=sum1+q1.pop(0).data
                if len(q2) is not 0:
                    sum1=sum1+q2.pop(0).data
                if len(q3) is not 0:
                    current3 = q3[0]
                    #print("inner data",current3.data)
                    if current3.left:
                        q3.append(current3.left)
                        #sum2=sum2+current3.left.data
                    if current3.right:
                        q3.append(current3.right)
                        #sum2=sum2+current3.right.data
                    sum2=sum2+q3.pop(0).data
        return sum1,sum2            
    def Count_nodes(self,node,count):
        count =count+1
        if node.left:
            count =  self.Count_nodes(node.left,count)
        if node.right:
            count = self.Count_nodes(node.right,count)   
        return count
    def CheckIfBinaryTreeSplitsinTwoHalves(self,node,n):
        if node is None:
            return 1
        s = self.CheckIfBinaryTreeSplitsinTwoHalves(node.left,n) +self.CheckIfBinaryTreeSplitsinTwoHalves(node.right,n)+1
        if n-s == s:
            self.checkifBTiseinhalf=True
        return s    
    def ConstructFromNPost(self,prearr,postarr):
        val =  prearr[self.preindex]
        node =Node(val)
        self.preindex=self.preindex+1
        if len(postarr)==1:
            return None
        postindex= postarr.index(prearr[self.preindex])
        leftpostarr = [postarr[i] for i in range(0,postindex+1)]
        rightarr = [postarr[i] for i in range(postindex+1,len(postarr)-1)]
        node.left = self.ConstructFromNPost(prearr,leftpostarr)
        node.right = self.ConstructFromNPost(prearr,rightarr)
        return node   
    def CheckInorderTraversalisTrue(self,node,index,inarr):
        if node.left:
            self.CheckInorderTraversalisTrue(node.left)
        inval = inarr[index]
        if inval is not node.data:
            self.check=False
        if node.right:
            self.CheckInorderTraversalisTrue(node.right)       
    def CheckLevelOrderisMinHeap(self,levelarr):
        ifminheap=False
        for i in range(0,len(levelarr)):
            rootdata = levelarr[i]
            if 2*i+2<len(levelarr):
                if rootdata<levelarr[2*i+1] and rootdata < levelarr[2*i+2]:
                    ifminheap=True
        return ifminheap
    def CheckLeafTwoOfBinaryTreeISSame(self,node1,node2,node1leaves,node2leaves):
        node1leaves = self.GetLeavesOFBinaryTree(node1,node1leaves)
        node2leaves = self.GetLeavesOFBinaryTree(node2,node2leaves)
        return node1leaves,node2leaves
    def GetLeavesOFBinaryTree(self,node,arr):
        if node is None:
            return arr
        if node.left is None and node.right is None:
            arr.append(node.data)
        if node.left:
            arr = self.GetLeavesOFBinaryTree(node.left,arr)
        if node.right:
            arr=self.GetLeavesOFBinaryTree(node.right,arr)
        return arr            
    def GetPreporderArrayofSuperTree(self,node,arr,rootvalofsubtree,checkforRootval):
        if node is None:
            return arr
        if node.data == rootvalofsubtree and checkforRootval is False:
            checkforRootval=True
            temp =node
            arr = self.GetPreporderArrayofSuperTree(temp,arr,rootvalofsubtree,checkforRootval)
            return arr
        if checkforRootval:
            arr.append(node.data)
        if node.left:
           arr =  self.GetPreporderArrayofSuperTree(node.left,arr,rootvalofsubtree,checkforRootval)
        if node.right:
           arr = self.GetPreporderArrayofSuperTree(node.right,arr,rootvalofsubtree,checkforRootval)
        return arr
    def CheckTreeisSubtree(self,tree,subtree):
        arr = self.GetPreporderArrayofSuperTree(tree,[],subtree.data,False)
        print(arr)
        arr2 =self.CheckviaPreorderTraversal(subtree,[])
        print(arr2)
        if arr==arr2:
            return True
        else:
            return False    
    def CheckviaPreorderTraversal(self,node,arr):
        if node is None:
            return arr
        arr.append(node.data)    
        if node.left:
            arr =self.CheckviaPreorderTraversal(node.left,arr)
        if node.right:
            arr =self.CheckviaPreorderTraversal(node.right,arr)
        return arr
    def PrintLongestLeafToLeafPath(self,node,arr1,arr2,l1,l2):
        if node.left:
            arr1,l1 = self.PrintLongestLeafToLeafPath(node.left,arr1,arr2,l1,l2)
        if node.right:
            arr2,l2 = self.PrintLongestLeafToLeafPath(node.right,arr1,arr2,l1,l2)
        if node.left is None and node.right is None:
            #print("aaya" ,node.data)
            return [node.data],1
        if node.left and node.right:
            if l1==l2:
                print(arr1[0])
            if l1>l2:
                print(arr1[0])
            if l1<l2:
                print(arr2[0])
            return [node.data],l1+l2
        if node.left and node.right is None:
            print(arr1,arr2,l1,l2)
            print(arr1[0])
            return [node.data],l1
        if node.right and node.left is None:
            print(arr1,arr2,l1,l2)
            print(arr2[0])
            return [node.data],l2       
    def PrintLongestLeafPathToRoot(self,node,arr1,arr2):
        if node.left:
           arr1 = self.PrintLongestLeafPathToRoot(node.left,arr1,arr2)
        if node.right:
           arr2= self.PrintLongestLeafPathToRoot(node.right,arr1,arr2)
        if node.left is None and node.right is None:
            return [node.data] 
        if len(arr1)==len(arr2):  
            arr1.append(node.data)
            return arr1
        if len(arr1)>len(arr2):
            arr1.append(node.data)
            return arr1
        if len(arr1)<len(arr2): 
            arr2.append(node.data)
            return arr2   
    def PrintLongestLeafPath(self,node):
        if node is None:
            return 0
        l1 = self.PrintLongestLeafPath(node.left)
        l2 = self.PrintLongestLeafPath(node.right)
        if l1+l2+1>self.preindex:
            self.preindex = l1+l2+1
        return 1+max(l1,l2)
    def PrintVerticalOrderTree(self,node,keepleft):
        if keepleft:
            self.keepverticalarrayL.append(node.data)
            self.keepverticalarrayR=[]
        if node.left:
            self.PrintVerticalOrderTree(node.left,True)
        if len(self.keepverticalarrayL)>0:
            print("left",self.keepverticalarrayL)
            print(self.keepverticalarrayL.pop())
        if len(self.keepverticalarrayR)>0:
            print("right",self.keepverticalarrayR)
            print(self.keepverticalarrayR.pop())    
        if node.right:
            self.keepverticalarrayR.append(node.right.data)
            self.PrintVerticalOrderTree(node.right,False)
    def getVerticalOrder(self,root, hd, m):
 
    # Base Case
        if root is None:
            return
        
        # Store current node in map 'm'
        try:
            m[hd].append(root.data)
        except:
            m[hd] = [root.data]
        
        # Store nodes in left subtree
        self.getVerticalOrder(root.left, hd-1, m)
        
        # Store nodes in right subtree
        self.getVerticalOrder(root.right, hd+1, m)
 
    def printVerticalOrder(self,root):
     
    # Create a map and store vertical order in map using
    # function getVerticalORder()
        m = dict()
        hd = 0
        self.getVerticalOrder(root, hd, m)
        
        # Traverse the map and print nodes at every horizontal
        # distance (hd)
        for index, value in enumerate(sorted(m)):
            for i in m[value]:
                print(i),
            print        
        
    def VerticalOrderTraversal(self,node):
        q=[]
        obj = {"val":node,"d":0}
        q.append(obj)
        dictmap={}
        while len(q) is not 0:
            current = q[0]
            key = current["d"]
            try:
               dictmap[key].append(current["val"].data)
            except:
               dictmap[key]=[current["val"].data]
            if current["val"].left:
                q.append({"val":current["val"].left,"d":key-1})
            if current["val"].right:
                q.append({"val":current["val"].right,"d":key+1})
            q.pop(0)
        for key in sorted(dictmap):
            print(dictmap[key])
    def VerticalOrderTraversalParticularOrder(self,node):
        q=[]
        obj = {"val":node,"d":0}
        q.append(obj)
        dictmap={}
        while len(q) is not 0:
            current = q[0]
            key = current["d"]
            print("dictmap",dictmap)
            print(key)
            try:
               
               old=dictmap[key-1]
               print("ert1",old)
               old.append(current["val"].data)
               print("ert2",old)
               dictmap[key]=old
            except:
               dictmap[key]=[current["val"].data]
            if current["val"].left:
                q.append({"val":current["val"].left,"d":key-1})
            if current["val"].right:
                q.append({"val":current["val"].right,"d":key+1})
            q.pop(0)
        for key in sorted(dictmap):
            print(dictmap[key])        


        # if l1>l2:
        #     arr1.append(node.data) 
        #     return l1+1,arr1
        # if l2>l1:
        #     arr2.append(node.data)
        #     return l2+1,arr2
        # if l1==l2:
        #     arr1.append(node.data)
        #     return l1+1,arr1
            
                           


                                  

# root = Node(10)  
# root.left = Node(8)  
# root.right = Node(2)  
# root.left.left = Node(3)  
# root.left.right = Node(5)  
# root.right.right = Node(2)
# 
# root = Node(26)  
# root.left = Node(10)  
# root.right = Node(3)  
# root.left.left = Node(4)  
# root.left.right = Node(6)
# root.left.right.left = Node(1)  
# root.right.right = Node(2) 
# root.right.right.left = Node(1) 

# root = Node(8)  
# root.left = Node(3)  

# root.left.left = Node(1)  
# root.left.right = Node(6)  
# root.left.right.left = Node(4)  
# root.left.right.right = Node(7)  

# root.right = Node(10)  
# root.right.right = Node(14)  
# root.right.right.left = Node(13) 
# root = Node(5) 
# root.left = Node(1) 
# root.right = Node(6) 
# root.left.left = Node(3) 
# root.right.left = Node(7) 
# root.right.right = Node(4) 
# # root.right.right.left = Node(4) 
check = CheckClass()
# sizen = check.Count_nodes(root,count=0)
# check.CheckIfBinaryTreeSplitsinTwoHalves(root,sizen)
#levarr =[30, 56, 22, 49, 30, 51, 2, 67]
# root1 = Node(1)  
# root1.left = Node(2)  
# root1.right = Node(3)  
# root1.left.left = Node(4)  
# root1.right.left = Node(6)  
# root1.right.right = Node(7)  

# root2 = Node(0)  
# root2.left = Node(1)  
# root2.right = Node(5)  
# root2.left.right = Node(4)  
# root2.right.left = Node(6)  
# root2.right.right = Node(7)
# T = Node('a') 
# T.left = Node('b') 
# T.right = Node('self.preindex') 
# T.left.left = Node('c') 
# T.right.right = Node('e') 

# S = Node('a') 
# S.left = Node('b') 
# S.left.left = Node('c') 
# S.right = Node('self.preindex')
# root = Node(1)
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.left.left = Node(12) 
# root.left.right = Node(5) 
# root.left.right.left = Node(6) 
# root.left.right.left.left = Node(10) 
# root.left.right.right = Node(7) 
# root.left.left.right = Node(8) 
# root.left.left.right.left = Node(9)

root =   Node(1); 
root.left =   Node(2); 
root.right =   Node(3); 
root.left.left =   Node(4); 
root.left.right =   Node(5); 
root.right.left =   Node(6); 
root.right.right =   Node(7); 
root.right.left.right =   Node(8); 
root.right.left.left =   Node(10);
root.right.right.right =   Node(9);
root.right.right.left =   Node(11);  
#check.PrintVerticalOrderTree(root,True)
check.VerticalOrderTraversalParticularOrder(root)
#print(check.preindex)
#print(check.CheckTreeisSubtree(T,S))
#check.CheckBinarySumTree(root)
##summ,issumtree =check.CheckBinarySumTree(root)
#sum1,sum2 = check.CheckSumCoverdNUncovered(root)
#print(sum1,sum2)