def inputNumberOfStd():
    std = int(input("Enter the Number of students: "))
    return std


ids = []
names = []
dobs = []


def inputStd(std):
    for i in range(std):
        id = input("Enter Id: ")
        name = input("Enter Name: ")
        dob = input("Enter date of birth: ")

        ids.append(id)
        names.append(name)
        dobs.append(dob)


def inputNumberOfCourse():
    course = int(input("Enter the Number of courses: "))
    return course


Courses = {
    "ids": [],
    "names": []
}


def inputCourse(course):
    for i in range(course):
        id = input("Enter Course Id: ")
        name = input("Enter Course Name: ")


        Courses["ids"].append(id)
        Courses["names"].append((name))


def listingCourse():
    print("List of courses are:")
    print(Courses["names"])


def listingStd():
    for i in range(len(ids)):
        print("Student Id of Student "+str(i+1)+": "+ids[i])
        print("Student Name of Student "+str(i+1)+": "+names[i])
        print("Student Date Of Birth of Student "+str(i+1)+": "+dobs[i])


def choseCourse():
    Course=input("Enter the course name: ")
    return Course


Marks = {
    "name" : [],
    "mark" : []
}


def inputMark(Course):
    for i in range(len(Courses)):
        if Course == Courses["names"][i]:
            for j in range(len(ids)):
                mark = input("Enter the mark of student "+str(j+1)+": ")
                Marks["name"].append(names[j])
                Marks["mark"].append(mark)


def showMarks(Course):
    for i in range(len(Courses)):
        if Course == Courses["names"][i]:
            print(Marks)


inputStd(inputNumberOfStd())
inputCourse(inputNumberOfCourse())
listingCourse()
listingStd()
inputMark(choseCourse())
showMarks(choseCourse())