x = 10
if x == 5:
    print ("x is five")
elif x == 10:
    print ("x is ten")
else:
    print ("x is neither five nor ten")

# match / case is available starting Python 3.10

# == -> equality check
# < > <= >= !=
# =
# + * / - **

print (3**4)

division = 10 / 3
print(division)

integer_division = 10 // 3
print(integer_division)

# Beware of floating point arithmetic 
x = 0.1
y = 0.2
z = 0.3
t = x + y

if 0.1 + 0.2 == 0.3:
    print ("Yay, I can add simple numbers")
else:
    print ("What?")

# for loop
for i in range(10):
    if i == 5:
        continue
    elif i == 8:
        break
    print(i)

print("range(5,10)")
for i in range(5, 10):
    print(i)

print("range(10,40,5)")
for i in range(10,40,5):
    print(i)

print("while loop")

i = 0
while i < 10:
    print(i)
    i += 1

# logical operators
# and, or, not
i = 25
if i > 10 and i < 30:
    print ("i is between 10 and 30")

# in operator
my_list = [3, 10, 9, 11]
search = int(input("Please enter number"))
if search in my_list:
    print ("I found it")
else:
    print ("It doesn't exist") 

my_dict = {
    "IE 201": "Z. Caner Taskin",
    "IE 202": "Tinaz Ekim"
}

search_class = input("Please enter class")
if search_class in my_dict:
    print (search_class + " is taught by " + my_dict[search_class])
else:
    print ("Instructor of " + search_class + " is not known" )

my_string = "I love Python"
if "Python" in my_string:
    print ("Found it in string!")
# note that string search is case sensitive
# note that operators act according to their precedence rules

