from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_details(self):
        pass



class Student(Person):
    def __init__(self, name, roll_number, marks):
        super().__init__(name)
        self.roll_number = roll_number
        self.__marks = marks  
    
    def get_marks(self):
        return self.__marks

    
    def set_marks(self, subject, mark):
        self.__marks[subject] = mark

    
    def total_marks(self):
        return sum(self.__marks.values())

    
    def average_marks(self):
        return self.total_marks() / len(self.__marks)

    
    def __gt__(self, other):
        return self.total_marks() > other.total_marks()

    def __lt__(self, other):
        return self.total_marks() < other.total_marks()

    def __eq__(self, other):
        return self.total_marks() == other.total_marks()

    
    def get_details(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}"



class GraduateStudent(Student):
    def __init__(self, name, roll_number, marks, thesis_topic):
        super().__init__(name, roll_number, marks)
        self.thesis_topic = thesis_topic

    
    def assign_grade(self):
        avg = self.average_marks()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def get_details(self):
        return f"Name: {self.name},\nRoll No: {self.roll_number},\nThesis: {self.thesis_topic}"



class Teacher(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    
    def assign_marks(self, student, subject, marks):
        student.set_marks(subject, marks)

    def get_details(self):
        return f"Teacher Name: {self.name}, Employee ID: {self.employee_id}"


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, roll_number):
        self.students = [s for s in self.students if s.roll_number != roll_number]

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_all_students_with_grades(self):
        print("##### Student Details #####")
        for student in self.students:
            if isinstance(student, GraduateStudent):
                print(f"{student.get_details()} | Total: {student.total_marks()} | "
                      f"Average: {student.average_marks():.2f} | Grade: {student.assign_grade()}")
            else:
                print(f"{student.get_details()} | Total: {student.total_marks()} | "
                      f"Average: {student.average_marks():.2f}")



if __name__ == "__main__":
    #Students
    s1 = GraduateStudent("Adersh", 101, {"Math": 90, "AI": 85, "ML": 88}, "Epileptic Seizure Detection")
    s2 = GraduateStudent("Rahul", 102, {"Math": 75, "AI": 70, "ML": 65}, "Image Classification")

    #Teacher
    t1 = Teacher("Mr. Joseph", "T01")

    #Teacher assign new marks
    t1.assign_marks(s2, "AI", 80)

    #School
    school = School()
    school.add_student(s1)
    school.add_student(s2)
    school.add_teacher(t1)

    
    school.display_all_students_with_grades()

    
    print("\n###### Comparison ######")
    print(f"{s1.name} > {s2.name}:", s1 > s2)
    print(f"{s1.name} == {s2.name}:", s1 == s2)
