class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" -> ")
                n = n.ref
            print("None")  # Indicates the end of the list

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(f"Node with data {x} is not present in the LinkedList")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_end(self):
        if self.head is None:
            print("we cant delete elements in empty linkedlist")
            return
        n=self.head
        while n.ref.ref is not None:
               n= n.ref
        n.ref= None




LL2 = LinkedList()

LL2.add_begin(100)
LL2.add_begin(200)
LL2.add_begin(300)
LL2.print_LL()
LL2.delete_end()
LL2.print_LL()


