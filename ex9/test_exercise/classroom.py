from student2 import Student

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


if __name__ == '__main__':
    classroom = Classroom()
    classroom.add_student(Student('1F10990123', 1))
    classroom.add_student(Student('1F10990456', 2))
    
    for st in classroom.students:
        print(st)