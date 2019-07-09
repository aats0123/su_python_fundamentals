if __name__ == '__main__':
    _input = input()
    transport_info = {}
    while _input != 'ready':
        city = _input.split(':')[0]
        if city not in transport_info.keys():
            transport_info[city] = {}
        vehicle_info = _input.split(':')[1].split(',')
        for element in vehicle_info:
            vehicle_type = element.split('-')[0]
            vehicle_capacity = int(element.split('-')[1])
            transport_info[city][vehicle_type] = vehicle_capacity
        _input = input()

    _input = input()
    while _input != 'travel time!':
        city = _input.split()[0]
        passengers = int(_input.split()[1])
        if sum(transport_info[city].values()) >= passengers:
            print(f'{city} -> all {passengers} accommodated')
        else:
            print(f'{city} -> all except {passengers - sum(transport_info[city].values())} accommodated')
        _input = input()
