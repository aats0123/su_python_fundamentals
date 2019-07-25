from point import *


class Point:
    def __init__(self, x, y):
        self.coord_x = int(x)
        self.coord_y = int(y)

    def __str__(self):
        return f'({self.coord_x}, {self.coord_y})'


class Rectangle:
    def __init__(self, l, t, w, h):
        self.left_upper = Point(l, t)
        self.right_bottom = Point(l + w, t + h)


def is_inside(r1, r2):
    condition1 = r1.left_upper.coord_x >= r2.left_upper.coord_x
    condition2 = r1.left_upper.coord_y >= r2.left_upper.coord_y
    condition3 = r1.right_bottom.coord_x <= r2.right_bottom.coord_x
    condition4 = r1.right_bottom.coord_y <= r2.right_bottom.coord_y
    return condition1 and condition2 and condition3 and condition4


r1_data = list(map(int, input().split()))
r2_data = list(map(int, input().split()))
rectangle1 = Rectangle(r1_data[0], r1_data[1], r1_data[2], r1_data[3])
rectangle2 = Rectangle(r2_data[0], r2_data[1], r2_data[2], r2_data[3])

if is_inside(rectangle1, rectangle2):
    print(f'Inside')
else:
    print(f'Not inside')
