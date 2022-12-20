print (hash(1))
print (hash(1.5))
print (hash("caner"))

class HashTable:
    def __init__(self) -> None:
        self.bucket_size = 100
        self.hash_table = [None] * self.bucket_size
    
    # O(1) on average
    def insert(self, key):
        index = hash(key) % self.bucket_size
        if self.hash_table[index] is None:
            self.hash_table[index] = []
        self.hash_table[index].append(key)
    
    # O(1) on average
    def find(self, key):
        index = hash(key) % self.bucket_size
        if self.hash_table[index] is None:
            return False
        else:
            return key in self.hash_table[index]


my_hash = HashTable()
# my_hash.insert(202032234245)
# my_hash.insert(535353532342)
# my_hash.insert(202032234245)

# return1 = my_hash.find(4353535)
# return2 = my_hash.find(535353532342)

my_hash.insert("IE 201")
my_hash.insert("IE 202")

return1 = my_hash.find("IE 203")

print(50)