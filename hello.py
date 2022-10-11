def factorial(n):
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

five_factorial = factorial(5)
print("5! = " + str(five_factorial))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

five_factorial_recursive = factorial_recursive(5)
print("5! (recursive) = " + str(five_factorial_recursive))


    