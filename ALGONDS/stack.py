# stacks
class Stack:
    def __init__(self):
        self.stack = []
    def Add(self,value):
        self.stack.append(value)
    def Pop(self):
        if len(self.stack)!=0:
            self.stack.pop()    
