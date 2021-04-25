from math import *

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
    def __init__(self, studentName, course, mark=0, credit=0 ,GPA=0):
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
        return "Student " + self.__studentName.getName() + " has a mark of " + str(
            self.getMark()) + " in " + str(self.__course)

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
