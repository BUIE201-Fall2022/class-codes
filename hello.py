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
def g(a, b = 5):
    print("a:", a)
    print("b:", b)

g(10, 10)
g(20)

