# Assignment 1: Design Your Own Class! 🏗️

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."


# Derived Class (Inheritance from Person)
class Student(Person):
    def __init__(self, name, age, student_id, course):
        # Call parent class constructor (inheritance)
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.__grade = None   # private attribute (encapsulation)

    # Method to set grade (encapsulation)
    def set_grade(self, grade):
        self.__grade = grade

    # Method to get grade (encapsulation)
    def get_grade(self):
        return self.__grade

    # Method to display student details
    def student_info(self):
        return f"Student: {self.name}, ID: {self.student_id}, Course: {self.course}"


# Another Derived Class to show polymorphism
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, course, thesis_title):
        super().__init__(name, age, student_id, course)
        self.thesis_title = thesis_title

    # Overriding method (polymorphism)
    def student_info(self):
        return f"Graduate Student: {self.name}, Thesis: {self.thesis_title}"

#example 
if __name__ == "__main__":
    # Create Student object
    s1 = Student("Yasmin", 20, "S123", "Computer Science")
    s1.set_grade("A")
    print(s1.introduce())        # from Person
    print(s1.student_info())     # from Student
    print("Grade:", s1.get_grade())

    # Create Graduate Student object
    g1 = GraduateStudent("Opiyo", 25, "G456", "Data Science", "AI in Healthcare")
    print(g1.introduce())        # from Person
    print(g1.student_info())     # overridden method in GraduateStudent
