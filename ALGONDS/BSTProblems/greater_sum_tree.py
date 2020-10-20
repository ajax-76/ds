class Node:
    def __init__(self,value):
        self.data = value
        self.left =None
        self.right =None
def SortedListToBalancedBST_2(arr):
    if len(arr) ==0:
        return None
    mid =int(len(arr)/2)
    root = Node(arr[mid])
    root.left=SortedListToBalancedBST_2(arr[:mid])
    root.right = SortedListToBalancedBST_2(arr[mid+1:])
    return root


store_val = []
succ_sum =[]
class MaxSumTree:
    def __init__(self):
        self.total_val = 0
        self.tocalval =0
        self.store_val = []
    def InorderNCal(self,root):
        if root.left:
            self.InorderNCal(root.left)
        #self.store_val.append(root.data)
        self.total_val=self.total_val+root.data
        if root.right:
            self.InorderNCal(root.right)
    # best method        
    def CalMaxMoreEfficient(self,root):
        if root.right:
            self.CalMaxMoreEfficient(root.right)
        self.tocalval=self.tocalval+root.data
        root.data = self.tocalval-root.data
        if root.left:
            self.CalMaxMoreEfficient(root.left)
    def CalBSTToBinaryTreeWithSome_2(self,root):
        if root.right:
            self.CalBSTToBinaryTreeWithSome_2(root.right)
        print(root.data)
        self.tocalval = self.tocalval+root.data
        root.data =  self.tocalval
        print("ll",root.data)
        if root.left:
            self.CalBSTToBinaryTreeWithSome_2(root.left)          
    def CalBSTToBinaryTreeWithSome_3(self,root):
        if root.left:
            self.CalBSTToBinaryTreeWithSome_3(root.left)
        self.tocalval = self.tocalval+root.data
        root.data =  self.tocalval
        if root.right:
            self.CalBSTToBinaryTreeWithSome_3(root.right) 
    def CalMaxTree(self,root):
        if root.left:
            self.CalMaxTree(root.left)
        print("nmSm",root.data)    
        self.tocalval=self.tocalval+root.data
        root.data = self.total_val-self.tocalval
        print("mxSm",root.data)
        if root.right:
            self.CalMaxTree(root.right)
    def PreOrderTraversal(self,root):
        print(root.data)
        if root.left:
            self.PreOrderTraversal(root.left)
        if root.right:
            self.PreOrderTraversal(root.right)

arr=[1,3,6,7,8,10,15,20,25,26,29,30,32]
arr2= [2,5,13]
arr3= [3,6,9,15,21]
tree =SortedListToBalancedBST_2(arr3)

Mxsumtree= MaxSumTree()
Mxsumtree.PreOrderTraversal(tree)
print("----------------------------")
#Mxsumtree.CalMaxMoreEfficient(tree)
#Mxsumtree.CalBSTToBinaryTreeWithSome_2(tree)
Mxsumtree.CalBSTToBinaryTreeWithSome_3(tree )
#Mxsumtree.CalMaxTree(tree)
Mxsumtree.PreOrderTraversal(tree)
#print(Mxsumtree.store_val)
#sum_tree = sum(store_val)
# print(sum_tree)
# def greater_sum_tree(node):
#     if node.left:
#         InorderNCal(node.left)
#     node.data = sum_tree
