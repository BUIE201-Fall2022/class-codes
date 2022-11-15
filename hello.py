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


row1 = [3, 2, 1]
row2 = [1, 6, 8]

m = [row1, row2]

print(m[0][2])

# matrix m, n

m = 3
n = 5
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(j)

print(type(matrix))
print(type(matrix[0]))
print(type(matrix[0][0]))
