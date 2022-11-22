class Array:
    def __init__(self) -> None:
        self._count = 0
        self._array = None
    
    # O(n)
    def insert(self, value):
        # create a bigger array -> O(1)
        new_count = self._count + 1
        new_array = [None] * new_count
        
        # copy existing elements to the new array -> O(n)
        for i in range(self._count):
            new_array[i] = self._array[i]
        
        # add the new value at the last index -> O(1)
        new_array[new_count - 1] = value

        # update member variables -> O(1)
        self._count = new_count
        self._array = new_array
    
    # equivalent to in operator on list
    # O(n)
    def find(self, value):
        for i in range(self._count):
            if self._array[i] == value:
                return True
        return False
    
    # O(1)
    def size(self):
        return self._count
    
    # O(1)
    def get_index(self, index):
        if index >= 0 and index < self._count:
            return self._array[index]
        # Error
        return None
        
my_array = Array()
my_array.insert(15)
my_array.insert(10)
my_array.insert(3)

result10 = my_array.find(10)
result20 = my_array.find(20)
