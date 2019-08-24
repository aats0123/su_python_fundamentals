import re
pattern = r'(?P<delimiter>32656 19759 32763) 0 (?P<repet>\d{1,2}) 0 (?P<letters>([1-9][0-9]{1,2} )+)'
regex = re.compile(pattern)

string = ''
_input = input()
while not _input == 'DEBUG':
    _input = _input.rstrip('\n') + ' '
    string += _input
    _input = input()

string = string.rstrip(' ')
matches = re.findall(pattern, string)

for match in matches:
    name = ''
    letters = match[2].split()
    for letter in letters:
        name += chr(int(letter))
    print(name)

