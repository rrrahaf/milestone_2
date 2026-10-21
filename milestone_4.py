class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        
    def display_info(self):
        print ("Name:", self.name)
        print ("ID:", self.student_id)
        print ("Grade:", self.grade)

class GraduateStudent(Student):
    def __init__(self, name, student_id, program_title):
        super().__init__(name, student_id)
        self.program_title=program_title

    def display_info(self):
        print("GRADUATE STUDENT")
        super().display_info()
        print("Program Title:", self.program_title)

class UndergraduateStudent(Student):
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)
        self.major=major
    def display_info(self):
        print("UNDERGRADUATE STUDENT")
        super().display_info()
        print("Major:", self.major)