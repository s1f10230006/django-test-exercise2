from student import Student

class INIADStudent(Student):
    def get_email(self):
        return "{}@iniad.org".format(self.id)


if __name__ == '__main__':
    st = INIADStudent('1F10990123', 2)
    print(st.id, st.grade)
    print(st.get_email())