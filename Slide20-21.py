def main():
    file = open("Python-Notes/Slides/text/hours.txt")
    lines = file.readlines()
    for line in lines:
        process_employee(line)


def process_employee(line):
    parts = line.split()
    id = parts[0]
    name = parts[1]
    sum = 0
    count = 0
    for i in range(2, len(parts)):
        sum += float(parts[i])
        count += 1
    average = round(sum/count, 2)
    print(name + " (ID#" + id + ") worked " + str(round(sum, 2)) +
          " hours (" + str(average) + ") hours/day")


main()
