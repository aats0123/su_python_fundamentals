import math

truck_width = float(input())
truck_depth = float(input())
truck_height = float(input())
number_of_barrels = int(input())

truck_volume = truck_width * truck_depth * truck_height

for i in range(number_of_barrels):
    barrel_radius = float(input())
    barrel_height = float(input())
    barrel_volume = math.pi * (barrel_radius ** 2) * barrel_height
    truck_volume -= barrel_volume
    if truck_volume > 0:
        continue
    elif truck_volume == 0:
        print(f'Truck is full. {i + 1} on board!')
    else:
        print(f'Truck is full. {i} on board!')
        break
if truck_volume >= 0:
    print(f'All barrels on board. Capacity left - {truck_volume:.2f}.')
