inventory = input().split()
_input = input()
while not _input == 'Fight!':
    command = _input.split()[0]
    equipment = _input.split()[1]
    if command == 'Buy':
        if not equipment in inventory:
            inventory.append(equipment)
    elif command == 'Trash':
        if equipment in inventory:
            inventory.remove(equipment)
    elif command == 'Repair':
        if equipment in inventory:
            inventory.remove(equipment)
            inventory.append(equipment)
    elif command == 'Upgrade':
        upgrade = equipment.replace('-', ':')
        equipment = equipment.split('-')[0]
        if equipment in inventory:
            index = inventory.index(equipment) + 1
            inventory[index:index] = [upgrade]

    _input = input()

print(' '.join([eq for eq in inventory]))
