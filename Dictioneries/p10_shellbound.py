if __name__ == '__main__':
    shells = {}
    _input = input()
    while _input != 'Aggregate':
        region = _input.split()[0]
        shell_size = int(_input.split()[1])
        if region not in shells.keys():
            shells[region] = []
        if shell_size not in shells[region]:
            shells[region].append(shell_size)
        _input = input()

    for region in shells.items():
        giant_shell = sum(region[1]) - int(sum(region[1]) / len(region[1]))
        print(f'{region[0]} -> ' + ', '.join([str(size) for size in region[1]]) + f' ({giant_shell})')
