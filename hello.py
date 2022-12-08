class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def insert(self, value):
        # base condition
        if self.next is None:
            self.next = ListNode(value)
        else:   # recursion
            self.next.insert(value)
    
    def find(self, value):
        # base condition
        if self.value == value:
            return True
        elif self.next is None:
            return False
        else:   # recursion
            return self.next.find(value)
    
    def size(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.size()
    
    def remove(self, value):
        # base condition
        if self.value == value:
            return self.next
        elif self.next is None:
            return self
        else:   # recursion
            self.next = self.next.remove(value)
            return self
    
    def print(self):
        print (str(self.value) + ", ", end="")
        if self.next is not None:
            self.next.print()
    
    def print_backward(self):
        if self.next is not None:
            self.next.print_backward()
        print (str(self.value) + ", ", end="")
class LinkedList:
    def __init__(self) -> None:
        self.root = None
    
    # O(1)
    def insert_begin(self, value):
        new_node = ListNode(value)
        new_node.next = self.root
        self.root = new_node
    
    # O(n)
    def insert_end(self, value):
        if self.root is None:
            self.root = ListNode(value)
        else:
            self.root.insert(value)
    
    # O(n)
    def find(self, value):
        if self.root is None:
            return False
        else:
            return self.root.find(value)
    
    # O(n)
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size()
    # O(n)
    def remove(self, value):
        if self.root is None:
            return
        else:
            self.root = self.root.remove(value)
    
    #O(n)
    def print(self):
        if self.root is None:
            return
        else:
            self.root.print()

    def print_backward(self):
        if self.root is None:
            return
        else:
            self.root.print_backward()


my_list = LinkedList()
my_list.insert_begin(15)
my_list.insert_begin(10)
my_list.insert_begin(5)
my_list.insert_begin(3)
my_list.insert_begin(20)

my_list.insert_end(40)

result5 = my_list.find(5)
result100 = my_list.find(100)

sz = my_list.size()

my_list.remove(10)

my_list.print()
my_list.print_backward()


i = 5