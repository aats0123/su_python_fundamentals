if __name__ == '__main__':
    command = input()
    output = {}
    while command != 'end':
        commands = command.split()
        if commands[2].isdigit():
            output[commands[0]] = int(commands[2])
        else:
            if commands[2] in output.keys():
                output[commands[0]] = output[commands[2]]

        command = input()

    print('\n'.join([f'{kvp[0]} === {kvp[1]}' for kvp in output.items()]))