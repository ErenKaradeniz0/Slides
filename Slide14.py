def is_prime(n):
    factors = 0
    for i in range(1, n+1):
        if (n % i == 0):
            factors += 1
    return factors == 2


# print(is_prime(199))


def both_odd(n1, n2):
    return n1 % 2 != 0 and n2 % 2 != 0


# de morgans law
# if not(7 == 5 and 5 > 3): #true
    # print(True)
# if 7 != 5 or 5 <= 3:  # true
    # print(True)


def is_vowel(n):
    n = n.lower()
    return (n == "a") or (n == "e") or (n == "i") or (n == "o") or (n == "u")


def is_not_vowel(n):
    n = n.lower()
    return not (n == "a") and not (n == "e") and not (n == "i") and not (n == "o") and not (n == "u")


# print(is_vowel("e"))
# print(is_not_vowel("g"))

# or


def is_not_vowel(n):
    n.n.lower()
    return not is_vowel(n)

# Strings


name = "Daffy Duck"
x = 3
y = 5
point = "("+str(x)+","+str(y)+")"
# print(point)

# name = "Ultimate"
# print(name[0], name[7], name[-8], name[-1])
# print(name[0:4], name[4:], name[:3])
# print(name[-4:-1], name[6:], name[:-2])

# print(name.find("mate"))
# print(name.find("team"))
# print(name.lower())
# print(name.upper())
# book = "Building Python Programs"
# print(book[9:15])


def name_border(name, size):
    for i in range(0,size):
            for i in range(0, name.find(" ")):
                print(name[i:name.find(" ")])
            for i in range(1, name.find(" ")+1):
                print(name[:i])
    for i in range(0, size):
        for i in range(0, len(name[name.find(" ")+1:])):
            print(name[name.find(" ")+1+i:len(name)])
        for i in range(0, len(name[name.find(" ")+1:])):
            print(name[name.find(" ")+1:name.find(" ")+2+i])

    


name_border("EREN KARADENİZ", 2)


# st1 = "Eren"
# for letter in st1:
#     print(letter)
# print(st1.startswith("Ere"), st1.endswith("en"), st1.endswith("e"), "re" in st1)

def ceaser_cipher(message, key):
    for i in range(0, len(message)):
        print(chr(ord(message[i])+key), end="")


# ceaser_cipher("Brad thinks Angelina is cute",3)
