class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.root = None
    
    # O(1)
    def insert_begin(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            new_node = ListNode(value)
            new_node.next = self.root
            self.root = new_node
    
    # O(n)
    def insert_end(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            new_node = ListNode(value)
            current_node = self.root
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

my_list = LinkedList()
my_list.insert_begin(15)
my_list.insert_begin(10)
my_list.insert_begin(5)
my_list.insert_begin(3)
my_list.insert_begin(20)

my_list.insert_end(40)

i = 5