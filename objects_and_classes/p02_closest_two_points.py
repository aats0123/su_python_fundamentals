from point import *


n = int(input())
points = [None]*n
for i in range(n):
    coordinates = list(map(int, input().split()))
    point = Point(coordinates[0], coordinates[1])
    points[i] = point

min_points = [None]*2
min_distance = float(sys.maxsize)
for i in range(n-1):
    for curr_point in points[i+1:]:
        points_distance = calculate_distance(points[i], curr_point)
        if points_distance < min_distance:
            min_distance = points_distance
            min_points[0] = points[i]
            min_points[1] = curr_point

print(f'{min_distance:.3f}')
print(min_points[0])
print(min_points[1])


