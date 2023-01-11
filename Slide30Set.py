thisset = set(("a", "b", "c","apple"))
myset = {"apple", "banana", "cherry", "a"}
print(thisset)
print(myset)
print()

print("this - my : differance")
print(thisset - myset)
print("or")
print(thisset | myset)
print("and")
print(thisset & myset)
print("exor")
print(thisset ^ myset)
print("apple" in myset)
print(len(myset))
print()

myset.add("orange")
print(myset)
myset.discard("apple")
print(myset)
myset.pop()
print(myset)

myset = {"apple", "banana", "cherry",}

for item in myset:
    print(item)