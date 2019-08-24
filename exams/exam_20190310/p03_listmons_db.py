def score(players_db, order):
    output = ''
    multiplier = 1
    if order == 'descending':
        multiplier = -1
    temp_db = sorted(players_db, key=lambda p: (p.points * multiplier, p.name))
    for p in temp_db:
        output += f'\n{p.name}: {p.points}'
    output = output.lstrip('\n')
    return output


def number_of_games(players_db, order):
    output = ''
    multiplier = 1
    if order == 'descending':
        multiplier = -1

    temp_db = sorted(players_db, key=lambda p: (p.games * multiplier, p.name))
    for p in temp_db:
        output += f'\n{p.name}: {p.games}'
    output = output.lstrip('\n')
    return output


command = {
    'score': score,
    'numberOfGames': number_of_games
}


class Player:
    def __init__(self, name, games, points):
        self.name = name
        self.games = games
        self.points = points


listmons_db = []
_input = input()

while not _input == 'report':
    _input = _input.split(' -> ')
    player_name = _input[0]
    games_results = _input[1].split(', ')
    games_number = len(games_results)
    total_points = sum([int(p) for p in games_results])
    player = Player(player_name, games_number, total_points)
    listmons_db.append(player)
    _input = input()

_input = input()
while not _input == 'end':
    sort_type = _input.split()[0]
    direction = _input.split()[1]
    print(command[sort_type](listmons_db, direction))
    _input = input()
