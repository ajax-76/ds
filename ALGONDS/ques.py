class Que:
    def __init__(self):
        self.que = []
    def Add(self,data):
        self.que.append(data)  
    def Pop(self):
        if len(self.stack)!=0:
            self.que.pop(0)
    def Front(self):
        return self.que[0]  


