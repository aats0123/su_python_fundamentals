class Exerise:
    def __init__(self, topic, course, contest_link, problems):
        self.topic = topic
        self.course = course
        self.contest_link = contest_link
        self.problems = problems.copy()


exercises = []
_input = input()
while not _input == 'go go go':
    _input = _input.split(' -> ')
    topic = _input[0]
    course = _input[1]
    contest_link = _input[2]
    problems = list(_input[3].split(', '))
    exercise = Exerise(topic, course, contest_link, problems)
    exercises.append(exercise)
    _input = input()

output = ''
for exercise in exercises:
    output += f'Exercises: {exercise.topic}\nProblems for exercises and homework for the "{exercise.course}" course @ SoftUni.\nCheck your solutions here: {exercise.contest_link}'
    for i in range(len(exercise.problems)):
        output += f'\n{i+1}. {exercise.problems[i]}'
    output += '\n'

print(output)
