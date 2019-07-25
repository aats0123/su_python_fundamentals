import math


class Point:
    def __init__(self, x, y):
        self.coord_x = int(x)
        self.coord_y = int(y)

    def __str__(self):
        return f'({self.coord_x}, {self.coord_y})'


def calculate_distance(point1, point2):
    h_dist = abs(point1.coord_x - point2.coord_x)
    v_dist = abs(point1.coord_y - point2.coord_y)

    return math.sqrt(h_dist**2 + v_dist**2)