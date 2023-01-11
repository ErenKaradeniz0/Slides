print("meow"*3)


def bake_cookies():
    print("baked")

def frost_cookies():
    print("cookies frozen")


for i in range(1, 6):  # repeat 5 times
    bake_cookies()
frost_cookies()

for i in range(1, 7):
    print(i, "squared =", i*i)

high_temp = 5
for i in range(-3, high_temp//2+1):  # -3 -2 -1 0 1 2
    print(i*1.8+32,end=(" "))


def my_method():
    print("\nT-minus", end=" ")
    for i in reversed(range(1, 11)):
        print(i, end=",")
    print("\nblastoff!")
    print("The end.")

my_method()


print("\nT-minus", end=" ")
for i in (range(10, 0,-1)):
        print(i, end=",")
print("\nblastoff!")
print("The end.")

#constants
DAYS_IN_WEEK = 7


def draw_shape(x):
    print("+",end="")
    for i in range(0,x):
        print("/\\/\\",end="")
    print("+")
    for i in range(0,x):
        print("|",end=" "*x*4)
        print("|")
    print("+",end="")
    for i in range(0,x):
        print("/\\/\\",end="")
    print("+")
draw_shape(10)

