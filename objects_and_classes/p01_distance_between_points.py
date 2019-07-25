from point import *


first_point_coords = list(map(int, input().split()))
second_point_coords = list(map(int, input().split()))

p1 = Point(first_point_coords[0], first_point_coords[1])
p2 = Point(second_point_coords[0], second_point_coords[1])

points_distance = calculate_distance(p1,p2)

print(f'{points_distance:.3f}')



