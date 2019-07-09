import string
def separate_string(_string):
    pattern = list(_string)
    separators = [',', ';', ':', '.', '!', '(', ')', '"', '\'', '\\', '/', '[', ']']
    words_list = [l for l in pattern if l not in separators]
    words_string = ''.join(l for l in words_list)
    return words_string.split()


def is_lowercase(_word):
    is_lowercase_word = True
    letters = list(_word)

    for l in letters:
        if l not in string.ascii_lowercase:
            is_lowercase_word = False
            break
    return is_lowercase_word


def is_uppercase(_word):
    is_uppercase_word = True
    letters = list(_word)

    for l in letters:
        if l not in string.ascii_uppercase:
            is_uppercase_word = False
            break
    return is_uppercase_word


if __name__ == '__main__':
    words = separate_string(input())
    lowercase_words = []
    uppercase_words = []
    mixed_words = []

    for word in words:

        if is_lowercase(word):
            lowercase_words += [word]
        elif is_uppercase(word):
            uppercase_words += [word]
        else:
            mixed_words += [word]

    if len(lowercase_words) > 0:
        print('Lower-case: ' + ', '.join(lowercase_words))
    if len(mixed_words) > 0:
        print('Mixed-case: ' + ', '.join(mixed_words))
    if len(uppercase_words) > 0:
        print('Upper-case: ' + ', '.join(uppercase_words))
