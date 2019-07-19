import math
class Point:
    def __init__(self, x, y):
        self.coord_x = int(x)
        self.coord_y = int(y)


def calculate_distance(point1, point2):
    h_dist = abs(point1.coord_x - point2.coord_x)
    v_dist = abs(point1.coord_y - point2.coord_y)

    return math.sqrt(h_dist**2 + v_dist**2)


first_point_coords = list(map(int, input().split()))
second_point_coords = list(map(int, input().split()))

p1 = Point(first_point_coords[0], first_point_coords[1])
p2 = Point(second_point_coords[0], second_point_coords[1])

points_distance = calculate_distance(p1,p2)

print(f'{points_distance:.3f}')



