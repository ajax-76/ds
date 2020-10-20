class DBLNode:
    def __init__(self,value):
        self.data = value
        self.next =None
        self.previous =None
class DBLinkedList:
    def __init__(self):
        self.head = None
        self.tail =None
    def addend(self,value):
        node =DBLNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            node.next = self.tail
            node.previous =self.head
            self.tail = node
        else:
            temp =self.tail
            node.next = self.tail
            node.previous = temp
            temp.next =node
            self.tail = node
    def TraversForward(self):
        current = self.head
        last = self.tail
        #print("tailval",last.data)
        while current.next is not last:
            print(current.data)
            current =current.next
        print(current.data)
        print(last.data)

class TerenaryNode:
    def __init__(self,value):
        self.data = value
        self.left=None
        self.middle =None
        self.right =None


class NaryTree:
    def __init__(self,value):
        self.data =value
        self.child =[]
        for i in range(10):
            self.child.append(None)

class NaryLeftChildRightChildNode:
    def __init__(self,value):
        self.data = value
        self.child = None
        self.Next =None
      

def PrintKthChild(root,k,p):
    pass



def ConstructdoublyLL(root,dbll):
    value =root.data
    dbll.addend(value)
    if root.left:
        ConstructdoublyLL(root.left,dbll)
    if root.middle:
        ConstructdoublyLL(root.middle,dbll)
    if root.right:
        ConstructdoublyLL(root.right,dbll)


root = NaryTree('A') 
root.child[0] = NaryTree('B') 
root.child[1] = NaryTree('C') 
root.child[2] = NaryTree('D') 
root.child[3] = NaryTree('E') 
root.child[0].child[0] = NaryTree('F') 
root.child[0].child[1] = NaryTree('G') 
root.child[2].child[0] = NaryTree('H') 
root.child[0].child[0].child[0] = NaryTree('I') 
root.child[0].child[0].child[1] = NaryTree('J') 
root.child[0].child[0].child[2] = NaryTree('K') 
root.child[2].child[0].child[0] = NaryTree('L') 
root.child[2].child[0].child[1] = NaryTree('M') 










# root = TerenaryNode(30)  
# root.left = TerenaryNode(5)  
# root.middle = TerenaryNode(11)  
# root.right = TerenaryNode(63)  

# root.left.left = TerenaryNode(1)  
# root.left.middle = TerenaryNode(4)  
# root.left.right = TerenaryNode(8)  

# root.middle.left = TerenaryNode(6)  
# root.middle.middle = TerenaryNode(7)  
# root.middle.right = TerenaryNode(15)  

# root.right.left = TerenaryNode(31)  
# root.right.middle = TerenaryNode(55)  
# root.right.right = TerenaryNode(65) 

# dbll = DBLinkedList()
# ConstructdoublyLL(root,dbll)
# dbll.TraversForward()
