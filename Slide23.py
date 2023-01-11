def reverse(numbers):
    for i in range(0, len(numbers)//2):
        temp = numbers[i]
        numbers[i] = numbers[len(numbers)-1-i]
        numbers[len(numbers)-1-i] = temp


def swap(numbers, a, b):
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp


def swap_all(list1, list2):
    length = len(list1)
    for i in range(0, length):
        temp = list1[i]
        list1[i] = list2[i]
        list2[i] = temp


numbers = [11, 42, 5, 27, 0, 89]
numbers2 = [5, 2, 554, 217, 54, 59]
reverse(numbers)
swap(numbers, 0, 1)
print(numbers)
print(numbers)

a1 = [12, 34, 56]
a2 = [20, 50, 80]


print(a1, a2)
swap_all(a1, a2)
print(a1, a2)


a1 = [12, 34, 56]
a2 = [20, 50, 80]

def merge(list1,list2):
    index=0
    for i in range(len(list1),len(list1)+len(list2)):
      list1.append(list2[index])
      index+=1
    return list1
def merge3(list1,list2,list3):
    a4=[0]*(len(list1)+len(list2)+len(list3))
    for i in range(0,len(list1)):
        a4[i]=list1[i]
    for i in range(0,len(list2)):
        a4[len(list1)+i]=list2[i]
    for i in range(0,len(list3)):
        a4[(len(list1)+len(list2)+i)]=list3[i]
    return a4
a=merge(a1,a2)

a1=[1,2,3,4]
a2=[5,6,7,8]
a3=[9,10,11,12]
a4=merge3(a1,a2,a3)
print(a4)