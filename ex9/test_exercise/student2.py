class Student:
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade

    def get_email(self):
        return f"{self.id}@toyo.jp"

    def __str__(self):
        return f"ID: {self.id}, Grade: {self.grade}"


if __name__ == '__main__':
    st = Student('1F10990123', 1)
    print(st)