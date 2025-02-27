class Student:
    #class attribute - shared by all instances of student
    #this is the same for every student

    school = "Shiz University"

    def __init__(self, name, age, grade):
        self.name = name #each student may have different name
        self.grade = grade #each student may have different grade
        self.age = age #each student may have different age

    #method to get information about student
    def get_info(self):
        return f"{self.name} is {self.age} and is a {self.grade} at {self.school}"
    
    #create student instances
student1 = Student("Alice", 22, "senior")
student2 = Student("Elphaba", 19, "freshman")
student3 = Student("Glinda", 20, "sophomore")

#print information about students
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())