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
    #Traversal pre_order
    def pre_order(self):
        print(self.key)
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    #deletion
    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if data <self.key:
            if self.lchild:
               self.lchild=self.lchild.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("node is not present in tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
    #to find smallest key in right sub tree
            node=self.rchild
            while node.lchild:
                self.key=node.key
            self.rchild=self.rchild.delete(node.key)


root=BST(100)
list1=[2,6,56,32,12,45]
for i in list1:
    root.insert(i)
print("pre_order")
root.pre_order()

print("After deleting")
root.delete(2)
root.pre_order()


