class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublyLL:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
           print("Linked List is empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref
    def print_LL_reverse(self):
        if self.head is None:
           print("Linked List is empty!")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n






dll=doublyLL()
dll.print_LL()
dll.add_begin(100)
dll.add_begin(120)
dll.add_begin(1080)

dll.print_LL()

