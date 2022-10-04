print ("Hello, IE 201!")
# name = input ("What is your name?")
# print ("Hello, " + name)

# This is a comment

"""
    This is a multi-line comment
    That can span multiple lines
"""

# Variable types
# String
my_string = "This is a string"
my_string2 = 'This is also a string'
my_string3 = "It's beautiful out there!"

# int
my_int = 3
# age_string = input ("How old are you?")
# print(type(age_string))
# age = int(age_string)
# print(type(age))

# float
my_float = 3.45
print(type(my_float))

# boolean
my_bool = True
my_bool2 = False
print(type(my_bool))

# data collections
# list
my_list = [2, 3, 10]
print(type(my_list))
print(my_list)
my_list[1] = 6
print(my_list)
my_list[0] = "this is a string in the same list with integers"
print(my_list)

# tuple
my_tuple = (3.3, 9.0, 4, "mixed types are ok")
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])
# my_tuple[0] = "test" #Cannot modify a tuple
print(my_tuple)

# dictionary
my_dict = {
    "IE 201" : "Z. Caner Taskin",
    "IE 202" : "Tinaz Ekim",
    "IE 203" : "Necati Aras"
}
print(type(my_dict))
print(my_dict)

current_class = input("Which class are you taking? ")
print(current_class + " is taught by " + my_dict[current_class])
my_dict["IE 201"] = "Tamer Unal"
print(my_dict)
