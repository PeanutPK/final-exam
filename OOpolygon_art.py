import turtle
import random

# Initial turtle and background
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)


class Polygon:
    def __init__(self):
        self.num_sides = random.randint(3, 5)
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300),
                         random.randint(-200, 200)]
        self.color = self.get_new_color
        self.border_size = random.randint(1, 10)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    @property
    def get_new_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))

    def reposition(self, reduction_ratio, poly):
        self.size *= reduction_ratio
        turtle.penup()
        move = 0
        if poly == 3:
            move = self.size * (1 - reduction_ratio)/3
        elif poly == 4:
            move = self.size * reduction_ratio
        elif poly == 5:
            move = self.size * (1 - reduction_ratio)
        turtle.forward(move)
        turtle.left(90)
        turtle.forward(move)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def triangle(self):
        self.num_sides = 3
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300),
                         random.randint(-200, 200)]
        self.color = self.get_new_color
        self.border_size = random.randint(1, 10)

    def square(self):
        self.num_sides = 4
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color
        self.border_size = random.randint(1, 10)

    def pentagon(self):
        self.num_sides = 5
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color
        self.border_size = random.randint(1, 10)

    def poly(self):
        self.num_sides = random.randint(3, 5)
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300),
                         random.randint(-200, 200)]
        self.color = self.get_new_color
        self.border_size = random.randint(1, 10)

    def one(self):
        for i in range(30):
            self.triangle()
            self.draw_polygon()

    def two(self):
        for i in range(30):
            self.square()
            self.draw_polygon()

    def three(self):
        for i in range(30):
            self.pentagon()
            self.draw_polygon()

    def four(self):
        for i in range(30):
            self.poly()
            self.draw_polygon()

    def five(self, num=30):
        for i in range(num):
            self.triangle()
            for j in range(3):
                self.draw_polygon()
                self.reposition(0.67, 3)

    def six(self, num=30):
        for i in range(num):
            self.square()
            for j in range(3):
                self.draw_polygon()
                self.reposition(0.5, 4)

    def seven(self, num=30):
        for i in range(num):
            self.pentagon()
            for j in range(3):
                self.draw_polygon()
                self.reposition(0.67, 5)

    def eight(self):
        self.five(10)
        self.six(10)
        self.seven(10)


# main
art_num = int(input("Which art do you want to generate? "
                    "Enter a number between 1 to 8,inclusive:"))
art = Polygon()
if art_num == 1:
    art.one()
elif art_num == 2:
    art.two()
elif art_num == 3:
    art.three()
elif art_num == 4:
    art.four()
elif art_num == 5:
    art.five()
elif art_num == 6:
    art.six()
elif art_num == 7:
    art.seven()
elif art_num == 8:
    art.eight()
elif 1 > art_num > 8:
    raise ValueError
else:
    raise TypeError

turtle.done()
