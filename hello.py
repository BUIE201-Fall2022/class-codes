def function_name():
    # function body
    print("Hello from function_name")

    # variables defined within functions are local unless explicitly declared global
    # do not use global variables!
    # global i
    i = 10
    print("i: " + str(i))

i = 5
function_name()
print("i: " + str(i))

def f(a):
    print(a)

f("Hello, f")
f(10)

# optional parameter with a default value
# default arguments have to come at the end
def g(a = 25, b = 15):
    print("a:", a)
    print("b:", b)

# positional argument passing
g(10, 10)
g(20)
g()

# parameter names explicitly given
g(a = 8, b = 4)
g(a = 9)
g(b = 45)

def sum_all(values):
    total = 0
    for i in values:
        total += i
    return total

total = sum_all([4, 5, 6])
print(total)

def sum_all2(a, *values):
    print("a: ", a)
    total = 0
    for i in values:
        total += i
    return total

total2 = sum_all2("x", 4, 5, 6)
print(total2)

total2 = sum_all2("y", 4, 5)
print(total2)
