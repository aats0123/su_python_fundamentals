gladiators = {}
marker = '->'

_input = input()
while not _input == 'Ave Cesar':
    if marker in _input:
        gladiator_data = _input.split(' -> ')
        gladiator = gladiator_data[0]
        technique = gladiator_data[1]
        skill = int(gladiator_data[2])
        gladiators[gladiator] = gladiators.get(gladiator, {})
        if technique not in gladiators[gladiator].keys():
            gladiators[gladiator][technique] = skill
        else:
            if skill > gladiators[gladiator][technique]:
                gladiators[gladiator][technique] = skill

    else:
        gladiator1 = _input.split(' vs ')[0]
        gladiator2 = _input.split(' vs ')[1]
        if gladiator1 not in gladiators.keys() or gladiator2 not in gladiators.keys():
            _input = input()
            continue
        else:
            techniques_gladiator1 = set(gladiators[gladiator1].keys())
            techniques_gladiator2 = set(gladiators[gladiator2].keys())
            common_techniques = techniques_gladiator1 & techniques_gladiator2
            if len(common_techniques) > 0:
                skills_gladiator1 = sum([sk for sk in gladiators[gladiator1].values()])
                skills_gladiator2 = sum([sk for sk in gladiators[gladiator2].values()])
                if skills_gladiator1 > skills_gladiator2:
                    gladiators.pop(gladiator2)
                elif skills_gladiator2 > skills_gladiator1:
                    gladiators.pop(gladiator1)

    _input = input()

sorted_gladiators = sorted(gladiators.keys(), key=lambda k:(-sum(gladiators[k].values()), k))
for gladiator in sorted_gladiators:
    total_skill = sum(gladiators[gladiator].values())
    print(f'{gladiator}: {total_skill} skill')
    techniques = gladiators[gladiator]
    sorted_technicues = sorted(techniques.keys(), key=lambda t: (-techniques[t], t))
    for t in sorted_technicues:
        print(f'- {t} <!> {techniques[t]}')