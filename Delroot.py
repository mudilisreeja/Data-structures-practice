class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    # Traversal
    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=" ")

    def delete(self, data):
        if self.key is None:
            print("We cannot delete from an empty tree")
            return None

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present")
        else:
            # Node with only one child or no child
            if self.lchild is None:
                return self.rchild
            elif self.rchild is None:
                return self.lchild

            # Node with two children: Get inorder successor (smallest in the right subtree)
            temp = self.rchild
            while temp.lchild:
                temp = temp.lchild

            # Copy the inorder successor's content to this node
            self.key = temp.key

            # Delete the inorder successor
            self.rchild = self.rchild.delete(temp.key)

        return self


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


# Create BST and test the implementation
root = BST(10)
elements = [6, 3, 7, 56, 25, 12]
for i in elements:
    root.insert(i)

print("Tree before deletion:")
root.in_order()
print("\nNode count:", count(root))

# Deleting root node
if count(root) > 1:
    root = root.delete(10)  # Update root after deletion
else:
    print("Cannot delete the root node as it's the only node.")
    root = None  # Explicitly set root to None if the tree becomes empty

# Perform in-order traversal if the tree is not empty
if root:
    print("\nTree after deletion:")
    root.in_order()
    print("\nNode count:", count(root))
else:
    print("\nTree is now empty.")
