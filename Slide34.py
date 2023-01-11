from random import *

vec = [2, 4, 6]
result = [3 * x for x in vec]
result2 = [3 * x for x in vec if x > 3]
result3 = [3 * x for x in vec if x < 2]
result4 = [[x, x ** 2] for x in vec]
result5 = [(x, x ** 2) for x in vec]

print(result)
print(result2)
print(result3)
print(result4)
print(result5)

words = ["aHMET", "yıLMaZ", "EFE", "dagdnn"]
capitalized = [word[0].upper() + word[1:].lower() for word in words]
print(capitalized)

vec = [2, 3, 4, 5, 6]
result = [x for x in vec if x % 2 == 0]
result = [x ** 2 for x in vec if x % 2 == 0 and x < 5]  # [4, 16]
print(result)
words = ["aHMET", "yıLMaZ", "EFE", "dagdnn", "göglföds", "fdksdfdsks", "fsdlklsşd"]
word3 = [word for word in words if len(word) > 3]
print(word3)

email = ["money", "rain", "money"]
spam_words = ["free", "money", "earn"]
spam_test = [1 for word in email if word in spam_words]
if len(spam_test) > 1:
    print("Spam Mail")

coin = [randint(0, 1) for i in range(0, 10)]
print(coin)

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
flattened = [i for row in matrix for i in row]
print(matrix)

vec = [2, 4, 6]
result = {3 * x for x in vec}
print(result)
vec2 = [2, 4, 6, 2, 2, 4, 3]
result2 = {3 * x for x in vec2}
print(result2)

original = {'two': 2, 'four': 4, 'six': 6}
org = {value: key for key, value in original.items()}
print(org)

