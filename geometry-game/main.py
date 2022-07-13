import point
import rectangle
from random import randint
import turtle

rectangle = rectangle.GuiRectangle(
    point.Point(randint(0,400), randint(0,400)),
    point.Point(randint(10,400), randint(10,400))
)

print(f'Rectangle Coordinates: {rectangle.point1.x}, {rectangle.point1.y}, and {rectangle.point2.x}, {rectangle.point2.y}')

user_point = point.GuiPoint(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess retangle area: "))

print(f'Your point was inside rectangle: {user_point.falls_in_rectangle(rectangle)}')
print(f'Your area was off by: {rectangle.area() - user_area}')

my_turtle = turtle.Turtle()

rectangle.draw(canvas=my_turtle)
user_point.draw(canvas=my_turtle)

turtle.done()

