wizards = {}

_input = input()
while not _input == 'fight':
    _input = _input.split()
    command = _input[0]
    wizard_name = _input[1]
    wizard_health = int(_input[2])
    wizard_damage = int(_input[3])
    if command == 'new':
        if wizard_name in wizards.keys():
            print('Wizard already exists!')
        else:
            wizards[wizard_name] = [wizard_health, wizard_damage]
    elif command == 'edit':
        if wizard_name not in wizards.keys():
            print('Wizard does not exist!')
        else:
            wizards[wizard_name][0] += wizard_health
            wizards[wizard_name][1] += wizard_damage


    _input = input()

_input = input()
while not _input == 'end':
    attacker_name = _input.split(' <=> ')[0]
    attacked_name = _input.split(' <=> ')[1]
    if attacked_name not in wizards.keys() or attacker_name not in wizards.keys():
        print('Cannot place a fight with non-existing wizards!')
    else:
        wizards[attacker_name][0] += 50
        wizards[attacked_name][0] -= wizards[attacker_name][1]
        if wizards[attacked_name][0] <= 0:
            wizards.pop(attacked_name)
            print(f'Fatality - {attacker_name} wins!')
        else:
            print(f'Next time {attacked_name}!')
    _input = input()

sorted_wizards_names = sorted(wizards.keys(), key=lambda w_n: -wizards[w_n][0])
for wizard in sorted_wizards_names:
    print(f'Wizard: {wizard}. Health: {wizards[wizard][0]}. Damage power: {wizards[wizard][1]}')
