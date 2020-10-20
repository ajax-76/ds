# # singly linked list
# class Node:
#     def __init__(self,value):
#         self.Value= value
#         self.Next = None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.Value)
#             printval = printval.Next
#     def addstart(self,value):
#         node = Node(value)
#         node.Next = self.headval
#         self.headval = node
#     def addend(self,value):
#         node = Node(value)
#         if self.headval is None:
#             self.headval = node
#             return
#         lastnode = self.headval # pointer
#         while lastnode.Next is not None:
#             lastnode = lastnode.Next
#         lastnode.Next = node       


# llist = SLinkedList()
# node2 = Node("ankit")
# node3 =Node("seth")
# llist.headval = node2
# node2.Next = node3
# llist.addstart("is happy")
# llist.addend("is happy")

# llist.listprint()
# add items 



#print(node1.Value,node2.Value,node1.Next.Value,node2.Next)


# doubly linked list 

class DNode:
    def __init__(self,value):
        self.Value= value
        self.Next = None,
        self.Previous =None
class DLinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def print_list_forward(self):
        current = self.headval
        while current is not self.tailval:
            print(current.Value)
            current = current.Next
        print(current.Value)    
    def print_list_backward(self):
        current = self.tailval
        #print(2,current.Value,self.headval.Previous.Value,current.Previous.Previous.Value)
        while current is not self.headval:
            print(current.Value)
            current = current.Previous
        print(current.Value)    
    def add_head(self,value):
        node = DNode(value)
        #print(value)
        node.Next = self.headval
        if self.headval:
            ll = self.headval
            ll.Previous = node
        self.headval= node
        node.Previous = self.headval
        if self.tailval is None:
            node.Next = self.tailval
            self.tailval  = node
            
    def add_end(self,value):
        node  = DNode(value)
        if self.tailval is None:
            node.Next = self.tailval
            self.headval = node
            node.Previous = self.headval
            self.tailval = node
        else:
            ll = self.tailval
            ll.Next= node
            node.Previous = ll
            node.Next = self.tailval
            self.tailval =node    
             


    
# headnode = DLinkedList()
# endnode = DLinkedList()
dll = DLinkedList()
dll2 = DLinkedList()
for i in range(4):
    dll.add_head('Ankit - '+ str(i) )
    dll2.add_end('Ankit - '+ str(i))
#dll.print_list_backward()
dll.print_list_backward()
print("-- -- - -- - - - -")
dll2.print_list_forward()
#print(node1.Value,node2.Value,node1.Previous,node2.Previous.Value,node1.Next.Value,node2.Next)