class Tree:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
root = Tree("root")
root.left = Tree("left")
root.right = Tree("right")        

