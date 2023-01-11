def print_letters(word):
    for letter in word[0:len(word)-1]:
        print(letter+",", end="")
    print(word[-1])


print_letters("Atmosphere")


def print_primes(max):
    if (max < 2):
        print()
    else:
        print(2, end="")
        for num in range(3, max+1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(", "+str(num), end="")


print_primes(50)
