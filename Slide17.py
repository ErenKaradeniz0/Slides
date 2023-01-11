n = 91
factor = 2
while n % factor != 0:
    factor += 1

# print("First factor is", factor)

SENTINEL = "quit"

sum = 0
response = input("type "+SENTINEL+" to exit:")
while response != SENTINEL:
    sum += len(response)
    response = input("type "+SENTINEL+" to exit:")
print("You typed a total of", sum, "characters")
