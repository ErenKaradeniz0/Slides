data = []
print(data)
data.append("bal")
data.append("honey")
data.append("sweetie")
print(data)

list = [2, 1, 1, 3, 3, 3, 4, 5, 6, 78, 78, 79]  # 12
print(list)


def remove_duplicates(list):
    i = 0
    while (i < len(list)-1):  # 0 1 2 3 4 .. 10   1 2  2 9        1  2
        if list[i] == list[i+1]:
            list.pop(i)
        else:
            i += 1
    return list

print(remove_duplicates(list))

name=("data","other_data",55)
tuple=("Tucson",80,90)
low=tuple[1]
# cant update tuple


