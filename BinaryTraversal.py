class BST:
    def __init__(self ,key ):
        self.key=key
        self.lchild=None
        self.rchild=None
#insertion
    def insert(self,data):
        if self.key is None:
           self.key=data
           return
        if self.key==data:
            return
        if self.key >data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
#Traversal pre-order method
    def pre_order(self):
        print(self.key)
        if self.lchild:
           self.lchild.pre_order()
        if self.rchild:
           self.rchild.pre_order()
#Traversal in-order method
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key)
        if self.rchild:
            self.rchild.in_order()
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key)


root=BST(10)
list1=[2,69,23,45,6,7,3]
for i in list1:
    root.insert(i)
print("preorder")
root.pre_order()
print("in order")
root.in_order()
print("post order")
root.post_order()
