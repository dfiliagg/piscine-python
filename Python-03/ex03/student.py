class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Student(Person):
    def __init__(self, fname, lname, course = None):
        super().__init__(fname, lname)
        self.course = course

    def __str__(self):
        if self.course != None:
            s = f"{self.fname} {self.lname} is registered to {self.course}"
        else:
            s = f"{self.fname} {self.lname} is not registered to any course"
        return s

def main():
    fname = input("Insert first name: ")
    lname = input("Insert last name: ")
    student = 0
    study = input("Are you a student? (y/n)")
    while study != "y" and study != "n":
        study = input('Please type "y" or "n": ')
    if study == "n":
        user = Person(fname, lname)
        print(user)
    else:
        course = input("Please insert your degree course: ")
        user = Student(fname, lname, course)
        print(user)

if __name__ == "__main__":
    main()