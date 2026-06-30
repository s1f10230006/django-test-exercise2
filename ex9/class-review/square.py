from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)


if __name__ == '__main__':
    s = Square(10)
    print(s.width, s.height)
    print(s.area())