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

#my_sorted_list = sorted(my_list)
#my_list.sort()

# O(n^2)
def bubble_sort(list):
    while True:
        print(list)
        already_sorted = True

        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                 list[i], list[i+1] = list[i+1], list[i]
                 already_sorted = False

        if already_sorted:
            break

my_list2 = my_list.copy()
bubble_sort(my_list2)
print(my_list2)
