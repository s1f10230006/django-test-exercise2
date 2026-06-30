class Student:
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade

    def get_email(self):
        return f"{self.id}@toyo.jp"


if __name__ == '__main__':
    st = Student('1F10990123', 1)
    print(st.id, st.grade)
    print(st.get_email())