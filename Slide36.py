from functools import reduce

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
print(squared)

mapsquared = list(map(lambda x: x ** 2, items))  # map
print(mapsquared)


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


print()
funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


def fahrenheit(T):
    return (float(9) / 5) * T + 32


def celsius(T):
    return (float(5) / 9) * (T - 32)


temp = (36.5, 37, 37.5, 39)
F = list(map(fahrenheit, temp))
C = list(map(celsius, F))
print(F)
print(C)

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = list(map(lambda x: (float(9) / 5) * x + 32, Celsius))
print(Fahrenheit)
C = list(map(lambda x: (float(5) / 9) * (x - 32), Fahrenheit))
print(C)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
map(lambda x, y: x + y, a, b)
map(lambda x, y, z: x + y + z, a, b, c)
map(lambda x, y, z: x + y - z, a, b, c)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = list(filter(lambda x: x % 2 == 0, fib))
print(result)
# result = [0, 2, 8, 34]
# from functools import reduce
print(reduce(lambda x, y: x + y, [47, 11, 42, 13]))

# max number
max = lambda a, b: a if (a > b) else b
print(reduce(max, [47, 11, 42, 102, 13]))
# Calculating the sum of the numbers from 1 to 100:
print(reduce(lambda x, y: x + y, range(1, 101)))

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# product = 24
print(product)
product2 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product2)

