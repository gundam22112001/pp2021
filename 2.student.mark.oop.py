
# Class
class Student:
    def __init__(self, id="", name="", dob=""):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def input(self):
        self.__id = input("Enter Student Id: ")
        self.__name = input("Enter Student Name: ")
        self.__dob = input("Enter Student Date of Birth: ")

    def __str__(self):
        return "Student: " + self.__name + " with id of " + self.__id + " born in " + self.__dob

    def describe(self):
        print(self.__str__())


class Mark:
    def __init__(self, studentName, course, mark=0):
        self.__studentName = studentName
        self.__course = course
        self.__mark = mark

    def input(self):
        print(f"Enter Student's mark for {self.__studentName}")
        self.__mark = input(f"in {self.__course}: ")

    def getMark(self):
        return self.__mark

    def getCourse(self):
        return self.__course

    def getName(self):
        return self.__studentName

    def __str__(self):
        return "Student " + self.__studentName.getName() + " has a mark of " + str(
            self.__mark) + " in " + self.__course

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name=""):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def input(self):
        self.__id = input("Enter Course Id: ")
        self.__name = input("Enter Course Name: ")

    def __str__(self):
        return "Course: " + self.__name + " with id of " + self.__id

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
                m = Mark(ClassRoom[j].getName(), ListOfCourse[i].getName())
                m.input()
                Marks.append(m)


# print the Mark for all student in a Course
def printMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark()])


# Main
inputMark(choseCourse())
inputMark(choseCourse())
printMark(choseCourse())
printMark(choseCourse())