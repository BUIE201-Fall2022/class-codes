import time

def factorial(n):
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

N = 990
iterative_start = time.time()
five_factorial = factorial(N)
iterative_end = time.time()
print("N! = " + str(five_factorial) + " computation time: " + str(iterative_end - iterative_start))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

recursive_start = time.time()
five_factorial_recursive = factorial_recursive(N)
recursive_end = time.time()
print("N! = " + str(five_factorial_recursive) + " computation time: " + str(recursive_end - recursive_start))


    