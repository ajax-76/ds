
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
def PreOrderTraversal(root):
    print(root.data)
    if root.left:
        PreOrderTraversal(root.left)
    if root.right:
        PreOrderTraversal(root.right)

list_for_min_heap=[]

def get_sorted_list_for_heap(root):
    if root.left:
        get_sorted_list_for_heap(root.left)
    list_for_min_heap.append(root.data)
    print(root.data)  
    if root.right:
        get_sorted_list_for_heap(root.right)    

def ConvertBST_TO_MinHEAP(root):
    if root is None:
        return None
    n1 = ConvertBST_TO_MinHEAP(root.left)
    n2 = ConvertBST_TO_MinHEAP(root.right)
    if n1 is None and n2 is None:
        n = Node(root.data)
        return n
    if n1 and n2:
        #print(n1.data,n2.data,root.data)
        cur = n1
        while cur.left is not None:
            cur =cur.left
        cur.left =Node(root.data)
        cur.right = n2
        #print("lvl")
        #LevelOrderTraversal(cur)
        return cur
    # if n1 and n2 is None:
    #     n1.left =Node(root.data)
    #     n1.right = None
    #     return n1 
    # if n1 is None and n2:
    #     n1.right =Node(root.data)
    #     n1.left = None
    #     return n1  
def LevelOrderTraversal(root):
    q=[]
    q.append(root)
    while(len(q)!=0):
        current = q[0]
        print(current.data)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        q.pop(0)       

# arr = [2,4,6,8,10,12,14]
# tree = SortedListToBalancedBST_2(arr)
# #PreOrderTraversal(tree) 
# get_sorted_list_for_heap(tree)
# print(list_for_min_heap)

root = Node(8)  
root.left = Node(4)  
root.right = Node(12)  
root.right.left = Node(10)  
root.right.right = Node(14)  
root.left.left = Node(2)  
root.left.right = Node(6)

minheapnode = ConvertBST_TO_MinHEAP(root)
LevelOrderTraversal(minheapnode)