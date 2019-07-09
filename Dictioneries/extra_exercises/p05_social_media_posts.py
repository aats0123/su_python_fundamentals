comments = {}
likes = {}
dislikes = {}


def post(info):
    post_name = info[0]
    comments[post_name] = {}
    likes[post_name] = 0
    dislikes[post_name] = 0


def like(info):
    post_name = info[0]
    likes[post_name] += 1


def dislike(info):
    post_name = info[0]
    dislikes[post_name] += 1


def comment(info):
    post_name = info[0]
    commenter_name = info[1]
    content = ' '.join([text for text in info[2:]])
    if commenter_name not in comments[post_name].keys():
        comments[post_name][commenter_name] = []
    comments[post_name][commenter_name].append(content)


if __name__ == '__main__':
    commands = {'post': post,
                'like': like,
                'dislike': dislike,
                'comment': comment}
    _input = input()
    while _input != 'drop the media':
        command = _input.split()[0]
        _info = _input.split()[1:]
        commands[command](_info)
        _input = input()

    for post in comments.items():
        print(f'Post: {post[0]} | Likes: {likes[post[0]]} | Dislikes: {dislikes[post[0]]}', '\nComments:')
        if len(post[1].keys()) == 0:
            print('None')
        else:
            for comment in post[1].items():
                print(f'*  {comment[0]}:', ', '.join([comm for comm in comment[1]]))
