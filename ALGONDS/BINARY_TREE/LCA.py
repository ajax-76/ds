class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class LCA:
    def __init__(self):
        self.lca = None
    def CalculateLCA(self,node,x1,x2):
        if node is None:
            return None
        l1 = self.CalculateLCA(node.left,x1,x2)
        l2 = self.CalculateLCA(node.right,x1,x2)

        if l1 is not None and l2 is not None:
                self.lca = node.data
                return None
        if l1 is not None and l2 is None:
            if node.data == x1 or  node.data ==x2:
                self.lca = node.data
            return l1
        if l1 is None and l2 is not None:
            if node.data == x1 or  node.data ==x2:
               self.lca = node.data
            return l2           
        if  node.data == x1:
            return x1
        elif node.data == x2:
            return x2
        else:
            return None
    def MaximumdifferenceBetweenNodeNAncestor(self,node,min_,max_):
        if node is None:
            if max_ is None and min_ is None:
                return 0
            return max_ - min_
        if max_ is None:
            max_=node.data
        if max_ is not None:
            if max_<node.data:
                max_=node.data
                min_=None
            if min_ is None:
                if node.left:
                    min_= node.left.data
                if node.right and min_ is None:
                    min_=node.right.data
            if min_ is not None:
                if min_>node.data:
                    min_=node.data        
        d1=self.MaximumdifferenceBetweenNodeNAncestor(node.left,min_,max_)            
        d2=self.MaximumdifferenceBetweenNodeNAncestor(node.right,min_,max_)            
        return max(d1,d2)

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 
# root.right.left = Node(6) 
# root.right.right = Node(7)


root = Node(8) 
root.left = Node(3) 

root.left.left = Node(1) 
root.left.right = Node(6) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 

root.right = Node(10) 
root.right.right = Node(14) 
root.right.right.left = Node(13)
root.right.right.left.left = Node(0)
lcaclass = LCA()
#lcaclass.CalculateLCA(root,6,7)
print(lcaclass.MaximumdifferenceBetweenNodeNAncestor(root,None,None))