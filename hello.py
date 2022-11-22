class Array:
    def __init__(self) -> None:
        self._count = 0
        self._array = None
    
    def insert(self, value):
        # create a bigger array
        new_count = self._count + 1
        new_array = [None] * new_count
        
        # copy existing elements to the new array
        for i in range(self._count):
            new_array[i] = self._array[i]
        
        # add the new value at the last index
        new_array[new_count - 1] = value

        # update member variables
        self._count = new_count
        self._array = new_array
        
my_array = Array()
my_array.insert(15)
my_array.insert(10)
my_array.insert(3)
