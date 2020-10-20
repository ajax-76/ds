class Que:
    def __init__(self):
        self.que = []
    def Add(self,data):
        self.que.append(data)  
    def Pop(self):
        if len(self.que)!=0:
            self.que.pop(0)
    def Front(self):
        return self.que[0]  
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    def Insert(self,value):
        if self.data:
            if value["i"] < self.data["i"]:
                if self.left:
                    self.left.Insert(value)
                else:
                    self.left= Node(value) 
            if value["i"] > self.data["i"]:
                if self.right:
                    self.right.Insert(value)
                else:
                    self.right=Node(value)                                        
    # def Insert(self,value):
    #     #print(value)
    #     if self.data:
    #         if value["i"]<self.data["i"]:
    #             if self.left is None:
    #                 self.left = Node(value)
    #             else:
    #                 self.left.Insert(value)
    #         if value["i"]>=self.data["i"]:
    #             if self.right is None:
    #                 self.right = Node(value)
    #             else:
    #                 self.right.Insert(value)
    #     else:
    #         self.data= value                  
    def PreOrderTraversal(self):
        print(self.data)
        if self.left:
            self.left.PreOrderTraversal()
        if self.right:
            self.right.PreOrderTraversal()                 
    def InOrderTraversal(self):
        if self.left:
            self.left.InOrderTraversal()
        print(self.data)
        if self.right:
            self.right.InOrderTraversal()
    def PostOrderTraversal(self):
        if self.left:
            self.left.PostOrderTraversal()
        if self.right:
            self.right.PostOrderTraversal()
        print(self.data)
    def Search(self,value):
        if self.data["i"] == value:
            print(self.data["j"])
        if value<self.data["i"] and self.left is not None:
            self.left.Search(value)
        if value>self.data["i"] and self.right is not None:
            self.right.Search(value)
        else:
            return
    def findMinFromNode(self,node):
        #self.right
        current = node
        while(current.left is not None):
            current = current.left
        return current
    def FinMin(self):
        current =self
        while current.left is not None:
            current =current.left
        return current.data["i"]
    def FindMinRecursion(self):
        #print(self.data["i"])
        if self.left is None:
            return self.data["i"]
        else:
            return self.left.FindMinRecursion()      
    def FinMax(self):
        current =self
        while current.right is not None:
            current =current.right
        return current.data["i"]
    def findMaxNode(self,node):
        current = node
        while current.right:
            current =current.right
        return current        
    def findHieght(self,node):
        if node is None:
            return 0
        left_height = self.findHieght(node.left)
        right_height = self.findHieght(node.right)
        return max(left_height,right_height)+1
    def Remove(self,current,value):
        #print(current.data,"dsdsd")
        if current is None:
            return current
        if value<current.data["i"]:
            #print("remove",current.data["i"])
            current.left =current.Remove(current.left,value)
        if value>current.data["i"]:
            current.right=current.Remove(current.right,value)
        elif value==current.data["i"]:
            print(current.data,"aswdecdvrgfvf")
            if current.right is None and current.left is None:
                current =None
                print("aya0")
                #return current
            elif current.right is None:
                temp= current
                current = current.left
                temp =None
            elif current.left is None:
                temp= current
                current =current.right
                temp = None
            else:
                min_node = self.findMinFromNode(current.right)
                current.data["i"]= min_node.data["i"]
                current.right = current.Remove(current.right,current.data["i"])
            #if current
        return current
    # my code -- - -  clean_code  - - - -   elegant code
    def Remove_2(self,value):
        #print("firaya",self.data["i"])
        if self is None:
            return self
        elif value<self.data["i"]:
            #print("aya",self.data["i"],self.left.data["i"])
            self.left =self.left.Remove_2(value)
        elif value>self.data["i"]:
            self.right = self.right.Remove_2(value)
        elif value==self.data["i"]:
            if self.left is None and self.right is None:
                #print("1 aya",self,self.data)
                self =None
                #print("1 aya",self)
            elif self.right is None:
                temp = self
                self =self.left
                temp =None
            elif self.left is None:
                temp = self
                self =self.right
                temp =None
            else:
                min_node = self.findMinFromNode(self.right)
                self.data["i"] = min_node.data["i"]
                self.right = self.right.Remove_2(self.data["i"])
                #self.Remove_2(min_node)            
        return self
    def LevelOrderTraverse(self):
        if self is None:
            return None
        que = Que()
        que.Add(self)
        while len(que.que)!=0:
            current = que.Front()
            print(current.data["i"])
            if current.left is not None:
                que.Add(current.left)
            if current.right is not None:
                que.Add(current.right)
            que.Pop()
    def findNode(self,value):
        if value == self.data["i"]:
            print("searchde",self.data["i"])
            return self
        elif value<self.data["i"] and self.left:
            return self.left.findNode(value)
        elif value>self.data["i"] and self.right:
            return self.right.findNode(value)

    def GetInorderSuccessor(self,value):
        current = self.findNode(value)
        if current:
            if current.right:
                min_val = self.findMinFromNode(current.right)
                return min_val.data["i"]
            else:
                ancestor =self
                successor = None
                while(ancestor!= current):
                    if current.data["i"]<ancestor.data["i"]:
                        successor =ancestor
                        ancestor =ancestor.left
                        #print("ancestor",ancestor.data["i"])
                    else:
                         ancestor =ancestor.right
                return successor.data["i"]
    def GetInorderPredecessor(self,value):
        current = self.findNode(value)
        if current:
            if current.left:
                find_node = self.findMaxNode(current.left)
                return find_node.data["i"]
            else:
                ancestor = self
                predesecor = None
                while ancestor!=current:
                    if current.data["i"]<ancestor.data["i"]:
                        ancestor = ancestor.left
                    else:
                        predesecor = ancestor 
                        ancestor=ancestor.right
                return predesecor.data["i"]   
                        
      
root =Node({"i":12,"j":"searched 12"})
arr2 =[{"i":7,"j":"searched 7"},{"i":3,"j":"searched 3"},{"i":10,"j":"searched 10"},{"i":11,"j":"searched 11"},{"i":8,"j":"searched 8"},{"i":18,"j":"searched 18"},{"i":14,"j":"searched 14"},{"i":20,"j":"searched 20"},{"i":1,"j":"searched 1"}]
#arr =[7,3,7,14,18,1,50,25,15]
for i in range(len(arr2)):
    root.Insert(arr2[i])

root.Search(8)
#root.PreOrderTraversal()
#root.PreOrderTraversal()
root.LevelOrderTraverse()
# print("Min Val",root.FinMin())
# print("Min Val Recur",root.FindMinRecursion())
# print("Max Val",root.FinMax())
# print("max hieght",root.findHieght(root))
#root.Remove_2(18)
# print("--------------")
# root.LevelOrderTraverse()

# print(root.GetInorderSuccessor(1))
# print(root.GetInorderPredecessor(3))
#print("--------------")
# root.InOrderTraversal()
# print("--------------")
# root.PostOrderTraversal()
#print("--------------")
#root.PreOrderTraversal()