def main():
    grades = {'Ali': [10, 16, 20, 13, 3, 17], 'Ken': [9, 16, 8, 19, 20, 20],
              'Daniel': [8, 10, 20, 20, 20, 20]}
    print(project_averages(grades))
    print(max_score(grades, "Ali"))


# takes a dictionary ofr student to list of grades as a parameter
# computes and returns the average grade for all assignments and all # students in the course
def average(grades):
    total = 0
    count = 0
    for student in grades:
        for grade in grades[student]:
            total += grade
        count += 1
        return total / count


# takes a dictionary ofr student to list of grades as a parameter
# returns a list of the averages for each project.
def project_averages(grades):
    averages = [0] * 6
    for student, grade_list in grades.items():
        for i in range(len(grade_list)):
            averages[i] += grade_list[i]
        for i in range(len(averages)):
            averages[i] /= len(grades)
        # the line below does the same thing as the loop above
        # naverages = [number / len(grades) for number in averages] return averages
        return averages


# takes a dictionary ofr student to list of grades as a parameter
# takes a student name as a parameter
# returns the number of the project that the student got their heighest # grade on.
def max_score(grades, student):
    student_grades = grades[student]
    grade_pairs = []
    for i in range(len(student_grades)):
        grade_pairs.append((student_grades[i], i + 1))
        grade_pairs.sort()
    return grade_pairs[-1][1]


main()
