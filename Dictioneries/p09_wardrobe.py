if __name__ == '__main__':
    wardrobe = {}
    n = int(input())
    for i in range(n):
        package = input().split(' -> ')
        color = package[0]
        clothes = package[1].split(',')
        if color not in wardrobe.keys():
            wardrobe[color] = {}
        for clothe in clothes:
            wardrobe[color][clothe] = wardrobe[color].get(clothe, 0) + 1

    required_clothe = input().split()
    req_color = required_clothe[0]
    req_clothe = required_clothe[1]
    for color in wardrobe.items():
        print(f'{color[0]} clothes:')
        for clothe in color[1].items():
            found = ''
            if color[0] == req_color and clothe[0] == req_clothe:
                found = ' (found!)'
            print(f'* {clothe[0]} - {clothe[1]}' + found)

