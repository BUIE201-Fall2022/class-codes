my_list = [3, 1, 6, 10, 4]

# linear search on list is O(n)
# in operator does linear search on lists
# find(my_list, 10)

my_sorted_list = [1, 3, 4, 6, 10]

# O(log n)
def binary_search(search, value):
    if len(search) == 0:
        return False
    left = 0
    right = len(search) - 1
    while True:
        if left == right:
            return search[left] == value
        elif right == left + 1:
            return search[left] == value or search[right] == value
        else:
            mid = (left + right) // 2
            if search[mid] == value:
                return True
            elif search[mid] > value:
                right = mid - 1
            else:
                left = mid + 1

print(my_sorted_list)
result6 = binary_search(my_sorted_list, 6)
result2 = binary_search(my_sorted_list, 2)