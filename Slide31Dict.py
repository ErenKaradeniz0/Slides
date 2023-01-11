my_dict = {"Romeo": "Montague",
           "Tyler": "Durden",
           "Tybalt": "Capulet",
           "Juliet": "Capulet"}
print(my_dict["Romeo"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.pop("Juliet"))
print(my_dict.items())
print(my_dict.popitem())
print(my_dict.items())
print("Romeo" in my_dict)  # key in dict
print("Capulet" in my_dict)
print(len(my_dict))

ages = {}
ages["Merlin"] = 4
ages["Chester"] = 2
ages["Percival"] = 12
for cat, age in ages.items():
    print(cat + "--> " + str(age))


def mystery(list1, list2):
    result = {}
    for i in range(0, len(list1)):
        result[list1[i]] = list2[i]
        result[list2[i]] = list1[i]
    return result


list1 = ["b", "l", "u", "e"]
list2 = ["s", "p", "o", "t"]
print(mystery(list1,list2))
