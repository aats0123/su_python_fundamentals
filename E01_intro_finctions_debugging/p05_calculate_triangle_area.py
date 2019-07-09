def calculate_triangle_area(base, height):
    area = base * height / 2
    return f'{area:.12g}'


if __name__ == '__main__':

    triangle_base = float(input())
    triangle_height = float(input())
    result = calculate_triangle_area(triangle_base, triangle_height)
    print(result)
