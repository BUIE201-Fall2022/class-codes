class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    # O(log n)
    def insert_recursive(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert_recursive(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert_recursive(value)
    
    # O(n)
    def size_recursive(self):
        left_size = 0
        if self.left:
            left_size = self.left.size_recursive()
        right_size = 0
        if self.right:
            right_size = self.right.size_recursive()
        
        return left_size + right_size + 1        

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert_recursive(value)
    
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size_recursive()

my_tree = Tree()
my_tree.insert(100)
my_tree.insert(50)
my_tree.insert(200)
my_tree.insert(30)
my_tree.insert(300)
my_tree.insert(150)
my_tree.insert(70)

size = my_tree.size()