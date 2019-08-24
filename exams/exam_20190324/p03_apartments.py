neighborhoods = {}
data = input()
while not data == 'collectApartments':
    data = data.split(' -> ')
    neighborhood_name = data[0]
    blocks = [int(el) for el in data[1].split(',')]
    for block in blocks:
        neighborhoods[neighborhood_name] = neighborhoods.get(neighborhood_name, {})
        neighborhoods[neighborhood_name][block] = [0, None]
    data = input()

data = input()
while not data == 'report':
    data = data.split(' -> ')
    neighborhood_name = data[0].split('&')[0]
    block = int(data[0].split('&')[1])
    number_of_apartments = data[1].split('|')[0]
    apartments_price = data[1].split('|')[1]
    if neighborhood_name in neighborhoods.keys() and block in neighborhoods[neighborhood_name].keys():
        neighborhoods[neighborhood_name][block][0] = number_of_apartments
        neighborhoods[neighborhood_name][block][1] = apartments_price
    data = input()
sorted_neighborhoods = sorted(neighborhoods.items(), key=lambda kvp: kvp[0])
for kvp in sorted_neighborhoods:
    print(f'Neighborhood: {kvp[0]}')
    for block in sorted(kvp[1]):
        print(f'* Block number: {block} -> {kvp[1][block][0]} apartments for sale. Price for one: {kvp[1][block][1]}')