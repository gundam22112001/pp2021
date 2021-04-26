from math import *


class Student:
    def __init__(self, id="", name="", dob="", GPA=0):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__GPA = GPA

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getGPA(self):
        return self.__GPA

    def setGPA(self, GPA):
        self.__GPA = GPA

    def input(self):
        self.__id = input("Enter Student Id: ")
        self.__name = input("Enter Student Name: ")
        self.__dob = input("Enter Student Date of Birth: ")

    def __str__(self):
        return "Student: " + self.__name + " with id of " + self.__id + " born in " + self.__dob

    def describe(self):
        print(self.__str__())


class Mark:
    def __init__(self, studentName, course, mark=0, credit=0, GPA=0):
        self.__studentName = studentName
        self.__course = course
        self.__credit = credit
        self.__mark = mark
        self.__GPA = GPA

    def input(self):
        print(f"Enter Student's mark for {self.__studentName}")
        self.__mark = float(input(f"in {self.__course}: "))
        self.__credit = Course.getCredit(course)

    def getMark(self):
        return floor(self.__mark * 10) / 10

    def getCourse(self):
        return self.__course

    def getGPA(self):
        return floor(self.__GPA * 10) / 10

    def setGPA(self, GPA):
        self.__GPA = GPA

    def getName(self):
        return self.__studentName

    def getCredit(self):
        return self.__credit

    def __str__(self):
        return "Student " + self.getName() + " has a mark of " + str(
            self.getMark()) + " in " + self.getCourse()

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name="", credit=0):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCredit(self):
        return self.__credit

    def input(self):
        self.__id = input("Enter Course Id: ")
        self.__name = input("Enter Course Name: ")
        self.__credit = int(input("Enter credit : "))

    def __str__(self):
        return "Course: " + self.__name + " with id of " + self.__id + " and credit of " + str(self.__credit)

    def describe(self):
        print(self.__str__())


# create arrays
ClassRoom = []
ListOfCourse = []
Marks = []

# find the number of students
NumberStd = int(input("Enter number of Students: "))

# adding Student objects into array ClassRoom
for i in range(NumberStd):
    s = Student()
    s.input()
    ClassRoom += [s]

# print out all the students in ClassRoom
for student in ClassRoom:
    print(student)

# find the number of courses
NumberOfCourse = int(input("Enter number of Courses: "))

# adding Course objects into array ListOfCourse
for i in range(NumberOfCourse):
    c = Course()
    c.input()
    ListOfCourse += [c]

# print out all the courses in ListOfCourse
for c in ListOfCourse:
    print(c)


# choose a course
def choseCourse():
    Course = input("Enter the course name: ")
    return Course


# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberStd):
                m = Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input()
                Marks.append(m)


# print the Mark for all student in a Course
def printMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark(), mark.getCredit()])


# choose student
def chooseStudent():
    stdName = input("Enter a Student's name: ")
    return stdName


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
    inputMark(choseCourse())

for course in ListOfCourse:
    print("-----Printing marks -----")
    printMark(choseCourse())

for std in ClassRoom:
    print("-----Calculating GPA -----")
    averageMark(chooseStudent())

arrSort()
