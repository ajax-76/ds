class Node:
    def __init__(self,value):
        self.data = value
        self.left =None
        self.right =None
    # def SortedListToBalancedBST(self,arr,start_index,end_index):
    #     n= end_index -start_index
    #     mid = start_index +int(n/2)
    #     val = arr[mid]
    #     if self.data is  None:
    #         print("aya")
    #         self =Node(val)
    #         print(self.data)
    #         self.SortedListToBalancedBST(arr,start_index,mid)
    #     if self.data:
    #         print("val" ,val)
    #         if val<self.data:
    #             if self.left:
    #                 self.left.SortedListToBalancedBST(arr,start_index,mid)
    #             else:
    #                 print(21,self.data,val)
    #                 self.left = Node(val)
    #                 self.left.SortedListToBalancedBST(arr,start_index,mid)
    #                 #print(22,self.left.data)
    #         if val>self.data:
    #             if self.right:
    #                 self.right.SortedListToBalancedBST(arr,mid,end_index)
    #             else:
    #                 print(22,self.data,val)
    #                 self.right = Node(val)
    #                 self.right.SortedListToBalancedBST(arr,mid,end_index)
    
def SortedListToBalancedBST_2(arr):
    if len(arr) ==0:
        return None
    mid =int(len(arr)/2)
    root = Node(arr[mid])
    root.left=SortedListToBalancedBST_2(arr[:mid])
    root.right = SortedListToBalancedBST_2(arr[mid+1:])
    return root

def PreOrderTraversal(node):
    if not node:
        return
    print("pre",node.data)
    if node.left:
        PreOrderTraversal(node.left)
    if node.right:
        PreOrderTraversal(node.right)         

arr=[1,3,6,7,8,10,15,20,25,26,29,30,32]

tree =SortedListToBalancedBST_2(arr)
#root.SortedListToBalancedBST(arr,0, len(arr)-1)
PreOrderTraversal(tree)