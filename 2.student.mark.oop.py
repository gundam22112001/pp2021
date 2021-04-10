class Student:
    def __init__(self, id = "", name = "", dob = ""):
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
        return "Student: "+self.__name+" with id of "+self.__id+" born in "+self.__dob


    def describe(self):
        print(self.__str__())


class Mark:
    def __init__(self, student, course, mark=0):
        self.__student = student
        self.__course = course
        self.__mark = mark


    def input(self):
        #self.__student = input("Enter the Student's Name: ")
        #self.__course = input("Enter the Course's Name: ")
        print(f"Enter Student's mark for {self.__student.getName()}")
        self.__mark = input(f"in {self.__course.getName()}: ")


    def getMark(self):
        return self.__mark


    def __str__(self):
        return "Student "+self.__student.getName()+" has a mark of "+str(self.__mark)+" in "+self.__course.getName()


    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id = "", name = ""):
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
        return "Course: "+self.__name+" with id of "+self.__id


    def describe(self):
        print(self.__str__())



NumberStd = int(input("Enter number of Students: "))
ClassRoom = []
ListOfCourse = []
for i in range(NumberStd):
    s = Student()
    s.input()
    ClassRoom +=[s]

for student in ClassRoom:
    print(student)

NumberOfCourse = int(input("Enter number of Courses: "))

for i in range(NumberOfCourse):
    c = Course()
    c.input()
    ListOfCourse +=[c]

for c in ListOfCourse:
    print(c)

m = Mark(ClassRoom[0],ListOfCourse[0])
m.input()
m.describe()

Marks = {
    "name" : [],
    "mark" : []
}

Course = input("Enter the course name: ")

for i in range(NumberOfCourse):
    if Course == ListOfCourse[i].getName():
        for j in range(NumberStd):
            m = Mark(ClassRoom[j], ListOfCourse[i])
            Marks["name"].append(ClassRoom[j].getName())
            m.input()
            Marks["mark"].append(m.getMark())


Course = input("Enter the course name: ")

for i in range(NumberOfCourse):
    if Course == ListOfCourse[i].getName():
        print(Marks)