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

fib5 = fibonacci(5)

fib5_recursive = fibonacci_recursive(5)

print(fibonacci_recursive)

N = 990
# iterative_start = time.time()
# five_factorial = factorial(N)
# iterative_end = time.time()
# print("N! = " + str(five_factorial) + " computation time: " + str(iterative_end - iterative_start))

# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)

# recursive_start = time.time()
# five_factorial_recursive = factorial_recursive(N)
# recursive_end = time.time()
# print("N! = " + str(five_factorial_recursive) + " computation time: " + str(recursive_end - recursive_start))


    