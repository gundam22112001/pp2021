from pw4.input import numberOfCourse, numberOfStd
import pw4.domain
from math import *
# create arrays
ClassRoom = []
ListOfCourse = []
Marks = []

# adding Student objects into array ClassRoom

NumberOfStd = numberOfStd()
NumberOfCourse = numberOfCourse()


for i in range(NumberOfStd):
    s = pw4.domain.Student()
    s.input()
    ClassRoom += [s]

# print out all the students in ClassRoom
for student in ClassRoom:
    print(student)

# adding Course objects into array ListOfCourse
for i in range(NumberOfCourse):
    c = pw4.domain.Course()
    c.input()
    ListOfCourse += [c]

# print out all the courses in ListOfCourse
for c in ListOfCourse:
    print(c)

# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberOfStd):
                m = pw4.domain.Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input(ListOfCourse[i])
                Marks.append(m)


# print the Mark for all student in a Course
def printMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark(), mark.getCredit()])


# average Mark
def averageMark(Name):
    x = y = 0
    for mark in Marks:
        if mark.getName() == Name:
            x += mark.getMark() * mark.getCredit()
            y += mark.getCredit()

    AverageMark = x / y
    AverageMark_fld = floor(AverageMark * 10) / 10
    print("Average Mark for " + Name + ": " + str(AverageMark_fld))

    for students in ClassRoom:
        if students.getName() == Name:
            students.setGPA(AverageMark_fld)


# array sorting
def arrSort():
    SortedArr = []

    for i in range(len(ClassRoom)):
        max_index = i
        for j in range(i + 1, len(ClassRoom)):
            if ClassRoom[max_index].getGPA() < ClassRoom[j].getGPA():
                max_index = j
        ClassRoom[i], ClassRoom[max_index] = ClassRoom[max_index], ClassRoom[i]

    for stds in ClassRoom:
        SortedArr.append(stds.getName())

    print("List of Student name in order of GPA from highest to lowest :")
    print(SortedArr)

# main
for course in ListOfCourse:
    print("-----Inputting marks -----")
    inputMark(pw4.input.choseCourse())

for course in ListOfCourse:
    print("-----Printing marks -----")
    printMark(pw4.input.choseCourse())

for std in ClassRoom:
    print("-----Calculating GPA -----")
    averageMark(pw4.input.chooseStudent())

arrSort()