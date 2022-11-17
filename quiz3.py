import random
import time

# O(N^2)
def check_duplicate_n2(check):
    n_elements = len(check)
    if (n_elements <= 1):
        return None
    for i in range(n_elements - 1):
        for j in range(i+1, n_elements):
            if check[i] == check[j]:
                return check[i]
    return None

def check_duplicates_nlogn(check):
    n_elements = len(check)
    if (n_elements <= 1):
        return None
    check_sorted = sorted(check)
    # in-place sorting of the original list check.sort()
    for i in range(n_elements - 1):
        if check_sorted[i] == check_sorted[i+1]:
            return check_sorted[i]
    return None

# O(n)
def check_duplicates_n(check):
    already_seen = set()
    for number in check:
        if number in already_seen:
            return number
        else:
            already_seen.add(number)
    return None

check = [1, -2, 4, 7, -3, 5, 4, 5]
result1n2 = check_duplicate_n2(check)
print(result1n2)
result1nlogn = check_duplicates_nlogn(check)
print(result1nlogn)
result1n = check_duplicates_n(check)
print(result1n)

check2 = [1, -2, 4, 7, -3, 5]
result2n2 = check_duplicate_n2(check2)
print(result2n2)
result2nlogn = check_duplicates_nlogn(check2)
print(result2nlogn)
result2n = check_duplicates_n(check2)
print(result2n)

for n in range(1000000, 1000005):
    randomlist = []
    for i in range(n):
        number = random.randint(0, 10*n)
        randomlist.append(number)
    start = time.time()
    check_duplicate_n2(randomlist)
    print(n, "check_duplicate_n2 ", time.time() - start)
    start = time.time()
    check_duplicates_nlogn(randomlist)
    print(n, "check_duplicate_nlogn ", time.time() - start)
    start = time.time()
    check_duplicates_n(randomlist)
    print(n, "check_duplicate_n ", time.time() - start)

