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
#searching
    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if self.key >data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the Tree!")






root = BST(10)
list1=[6,3,1,7,78]
for i in list1:
    root.insert(i)
root.search(3)