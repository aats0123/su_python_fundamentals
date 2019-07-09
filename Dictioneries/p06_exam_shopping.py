if __name__ == '__main__':
    stocking = input()
    inventory = {}
    while stocking != 'shopping time':
        product = stocking.split()[1]
        quantity = int(stocking.split()[2])
        inventory[product] = inventory.get(product, 0) + quantity
        stocking = input()

    buying = input()
    while buying != 'exam time':
        product = buying.split()[1]
        quantity = int(buying.split()[2])
        if product not in inventory.keys():
            print(f'{product} doesn\'t exist')
        elif inventory[product] <= 0:
            print(f'{product} out of stock')
        else:
            inventory[product] -= quantity
        buying = input()

    print('\n'.join([f'{kvp[0]} -> {kvp[1]}' for kvp in inventory.items() if kvp[1] > 0]))
