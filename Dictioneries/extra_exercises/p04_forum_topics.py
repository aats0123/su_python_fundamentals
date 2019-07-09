if __name__ == '__main__':
    forum = {}
    _input = input()
    while _input != 'filter':
        topic = _input.split(' -> ')[0]
        tags = set(_input.split(' -> ')[1].split(', '))
        if topic not in forum.keys():
            forum[topic] = tags
        else:
            for tag in tags:
                forum[topic].add(tag)

        _input = input()
    filter_tags = set(input().split(', '))
    for topic in forum.items():
        if topic[1] & filter_tags == filter_tags:
            print(f'{topic[0]} | #' + ', #'.join([tag for tag in topic[1]]))
    print()