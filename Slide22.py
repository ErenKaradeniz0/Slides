name = [1, 2, 3, 4]
print(name)

name = [5] * 5
print(name)

name [4]=4
print(name)

for i in range(0,5):
    name[i]=2*i
print(name)

for i in range(0,len(name)):
    print(str(name[i]),end=' ')
print()
for i in name:
    print(str(i),end=" ")

name.insert(0,31)
print(name)

name=[1,7,5,6,4,14,11]
print(name)
for i in range(0,len(name)-1):
    if(name[i]>name[i+1]):
        name[i+1]=name[i+1]*2
print(name)