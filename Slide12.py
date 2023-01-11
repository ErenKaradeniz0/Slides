def sum():
    sum = 0
    for i in range(1, 5):
        next = int(input("Type a number: "))
        sum += next  # cumulative sum
    print(sum)


def power():
    product = 1
    x = int(input("enter x number to x ^ n "))
    n = int(input("enter n number to x ^ n "))
    for i in range(1, n):
        product *= x
    print(x, "^", n, "=", product)


def meals():
    people = int(input("how many people ate "))
    subtotal = 0

    for i in range(1, people+1):
        person_cost = float(input("Person #"+str(i) +
                            ": How much did your dinner cost? "))
        subtotal += person_cost
    return subtotal


def results(subtotal):
    tax = subtotal * 0.08
    tip = subtotal * 0.15
    total = subtotal+tax+tip
    print("Subtotal : "+str(subtotal))
    print("Tax : "+str(tax))
    print("Tip : "+str(tip))
    print("Total : "+str(total))


# results(meals())


def count_factors(number):
    count = 0
    for i in range(1, number+1):
        if (number % i == 0):
            count+=1
    return count


print(count_factors(24))
