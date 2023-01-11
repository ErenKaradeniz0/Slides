def most_frequent_digit(number):
    count_list=[0]*10
    while number>0:
        digit=number%10
        count_list[digit]+=1
        number=number//10
    max=0
    for i in range(0,len(count_list)):
        if(max<count_list[i]):
            max=i
    return max

def main():
    file = open("text/sections.txt")
    lines =file.readlines()
    section=1
    for line in lines:
        points=count_points(line)
        grades=compute_grades(points)
        results(section,points,grades)
        section += 1

def count_points(line):
    points = [0]*5
    for i in range(len(line)):
        student = i % 5  #0 1 2 3 4
        earned = 0
        if line[i] == "y":
            earned = 3
        elif line[i] == "n":
            earned = 1
        points[student] = min(20, points[student] + earned)
    return points

def compute_grades(points):  
    grades=[0]*5
    for i in range(len(points)):
        grades[i]=100.0 * points[i]/20
    return grades


def results(section, points, grades):
    print("Section", section)
    print("Student points", points)
    print("Student grades", grades)
    print()

main()