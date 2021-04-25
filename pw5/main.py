import os
import zipfile
from math import *
import pw5.domain
from pw5.input import numberOfCourse, numberOfStd

# check if students.dat exist
if os.path.isfile('students.dat'):
        zip_file = zipfile.ZipFile('students.dat', 'r')
        zip_file.extractall()

# create arrays
ClassRoom = []
ListOfCourse = []
Marks = []

# input number of courses and students
NumberOfStd = numberOfStd()
NumberOfCourse = numberOfCourse()

# create new text files
f = open("students.txt", "w")
f.close()
g = open("courses.txt", "w")
g.close()
h = open("marks.txt", "w")
h.close()

# adding Student objects into array ClassRoom
for i in range(NumberOfStd):
    s = pw5.domain.Student()
    s.input()
    f = open("students.txt", "a")
    f.write("Student's Id: " + s.getId() + "\n")
    f.write("Student's Name: " + s.getName() + "\n")
    f.write("Date of Birth: " + s.getDob())
    f.close()
    ClassRoom += [s]

# print out all the students in ClassRoom
for student in ClassRoom:
    print(student)

# adding Course objects into array ListOfCourse
for i in range(NumberOfCourse):
    c = pw5.domain.Course()
    c.input()
    g = open("courses.txt", "a")
    g.write("Course's Id: " + c.getId() + "\n")
    g.write("Course's Name: " + c.getName() + "\n")
    g.write("credit: " + str(c.getCredit()) + "\n")
    g.close()
    ListOfCourse += [c]

# print out all the courses in ListOfCourse
for c in ListOfCourse:
    print(c)

# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberOfStd):
                m = pw5.domain.Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input(ListOfCourse[i])
                h = open("marks.txt", "a")
                h.write("Student's Name: " + m.getName() + "\n")
                h.write("Mark: " + str(m.getMark()) + "\n")
                h.close()
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

    for mark in Marks:
        if mark.getName() == Name:
            mark.setGPA(AverageMark_fld)


# array sorting
def arrSort():
    SortedArr = []

    for i in range(len(Marks)):
        max_index = i
        for j in range(i + 1, len(Marks)):
            if Marks[max_index].getGPA() < Marks[j].getGPA():
                max_index = j
        Marks[i], Marks[max_index] = Marks[max_index], Marks[i]

    for mark in Marks:
        SortedArr.append(mark.getName())

    print("List of Student name in order of GPA from highest to lowest :")
    print(SortedArr)

# main
for course in ListOfCourse:
    print("-----Inputting marks -----")
    inputMark(pw5.input.choseCourse())

for course in ListOfCourse:
    print("-----Printing marks -----")
    printMark(pw5.input.choseCourse())

for std in ClassRoom:
    print("-----Calculating GPA -----")
    averageMark(pw5.input.chooseStudent())

arrSort()

# zip all file end with .ext
zip_file = zipfile.ZipFile('students.dat', 'w')
for x in os.listdir():
    if x.endswith('s.txt'):
        zip_file.write(x, compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

