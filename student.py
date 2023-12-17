class Student():
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def update(self, name, marks):
        self.name = name
        self.marks = marks

class StudentCollection():
    def __init__(self):
        self.all_student = [Student("a", 1, 90),
                            Student("b", 2, 70),
                            Student("c", 3, 50),
                            Student("d", 4, 30)]

    def search(self, name):
        for student in self.all_student:
            if student.name == name:
                return student

    def delete(self, roll_no):
        for student in self.all_student:
            if student.roll_no == roll_no:
                self.all_student.remove(student)
                return True
        return False

    def first_position(self):
        student1 = []
        for student in self.all_student:
               if student.marks >= 80:
                 student1.append(student)
        return student1

    def low_grade(self):
         student2 = []
         for student in self.all_student:
              if student.marks < 33:
               student2.append(student)
         return student2
    def update_marks(self, roll_no, marks):
        for student in self.all_student:
            if student.roll_no == roll_no:
             student.marks = marks
             return True
        return False
    def register(self, name, marks):
        max_rollno = 0
        for student in self.all_student:
            if student.roll_no > max_rollno:
                max_rollno = student.roll_no
        student_x = Student(name, max_rollno+1, marks)
        self.all_student.append(student_x)
        return True

student_collection_x = StudentCollection().register("e",60)
print(student_collection_x)