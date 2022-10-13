import time

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    prevprev = 1
    prev = 1
    current = 2
    i = 3 # iteration counter
    while i <= n:
        current = prev + prevprev
        prevprev = prev
        prev = current
        i += 1
    return current

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    n1 = fibonacci_recursive(n-1) 
    n2 = fibonacci_recursive(n-2)
    return n1 + n2

def fibonacci_recursive_cache(n, cache):
    if n == 1 or n == 2:
        return 1
    if n in cache:
        return cache[n]
    
    result = fibonacci_recursive_cache(n-1, cache) + fibonacci_recursive_cache(n-2, cache)
    cache[n] = result
    return result

N = 40
iterative_start = time.time()
iterative_result = fibonacci(N)
iterative_end = time.time()
print("Iterative N = " + str(iterative_result) + " computation time: " + str(iterative_end - iterative_start))

recursive_cached_start = time.time()
recursive_cached_result = fibonacci_recursive_cache(N, {})
recursive_cached_end = time.time()
print("Recursive Cached N = " + str(recursive_cached_result) + " computation time: " + str(recursive_cached_end - recursive_cached_start))

recursive_start = time.time()
recursive_result = fibonacci_recursive(N)
recursive_end = time.time()
print("Recursive N = " + str(recursive_result) + " computation time: " + str(recursive_end - recursive_start))

