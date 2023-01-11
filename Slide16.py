def print_letters(word):
    print(word[0], end="")
    for i in range(1, len(word)):
        print(", " + word[i], end="")
    print()


print_letters("alfdsflşfsdk")


def average_temp(n):
    sum = 0
    for i in range(0, n):
        sum += int(input("temperature? "))
    avg = sum/n
    print("Average temperature:",avg)

average_temp(5)