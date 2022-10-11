def function_name():
    # function body
    print("Hello from function_name")

    # variables defined within functions are local unless explicitly declared global
    # do not use global variables!
    global i
    i = 10
    print("i: " + str(i))

i = 5
function_name()
print("i: " + str(i))

