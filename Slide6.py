def turtle(x):
    print("  _____")
    print(" /", x, x, "\\/*)")
    print("/", x, x, x, "\\/")
    print(" ou  ou")


turtle("V")


def counter(count):
    for i in range(1, count+1):
        print("printed", i, "times")


counter(5)  # must use integer for range

name = input("what is your name : ")

print("Your name is ", name)

age = int(input("how old are you? "))

years = 65-age

print(years, "years until retirement!")
