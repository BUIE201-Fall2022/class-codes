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
    
    # O(n)
    def find(self, value):
        if self.root == None:
            return False
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.value == value:
                    return True
                else:
                    current_node = current_node.next
            return False
    
    # O(n)
    def size(self):
        if self.root == None:
            return 0
        else:
            current_node = self.root
            count = 1
            while current_node.next is not None:
                current_node = current_node.next
                count += 1
            return count

    # O(n)
    def remove(self, value):
        if self.root == None:
            return
        else:
            current_node = self.root
            while current_node.next is not None:
                if current_node.next.value == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next
    
    def print(self):
        print("[", end="")
        if self.root is not None:
            current_node = self.root
            while current_node is not None:
                print (str(current_node.value) + ", ", end="")
                current_node = current_node.next
        print("]")



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

i = 5