print(issubclass(bool, int))

class Animal:
    pass

class Cat(Animal):
    pass

print(issubclass(Cat, Animal))

class Car:
    pass

my_car = Car()

print(type(my_car))
print(type(Car))
print(type(Animal))


print(issubclass(Car, Animal))

print(issubclass(int, float))

# floating point arithmetic is inexact
print (0.1 + 0.2 == 0.3)

# integer arithmetic is exact
print (1 + 2 == 3)

# everything is an object in Python
my_list = [3, "str"]

print(issubclass(int, object))
print(issubclass(str, object))
print(issubclass(list, object))

def f():
    pass

print(type(f))
