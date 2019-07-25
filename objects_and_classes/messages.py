users = []


class User:
    def __init__(self, username):
        self.username = username
        self.rcv_messages = []


class Message:
    def __init__(self, _content, sender_name):
        self.content = _content
        self.sender = sender_name


def is_user_valid(username):
    return username in [user.username for user in users]


_input = input()

while not _input == 'exit':
    _input = _input.split()
    if _input[0] == 'register':
        if not is_user_valid(_input[1]):
            user = User(_input[1])
            users.append(user)
    else:
        sender = _input[0]
        receiver_name = _input[2]
        content = _input[3]
        if not (is_user_valid(sender) and is_user_valid(receiver_name)):
            _input = input()
            continue
        else:
            message = Message(content, sender)
            user = [user for user in users if user.username == receiver_name][0]
            user.rcv_messages.append(message)
    _input = input()

_input = input().split()
username1 = _input[0]
username2 = _input[1]
user1 = [user for user in users if user.username == username1][0]
user2 = [user for user in users if user.username == username2][0]
user1_messages = [message.content for message in user1.rcv_messages if message.sender == username2]
user2_messages = [message.content for message in user2.rcv_messages if message.sender == username1]
user2_messages = list(map(lambda msg: username1 + ': ' + msg, user2_messages))
user1_messages = list(map(lambda msg: msg + ' :' + username2, user1_messages))
if len(user1_messages) == 0 and len(user2_messages) ==0:
    print('No messages')
else:
    n = min(len(user1_messages), len(user2_messages))
    for i in range(n):
        print(user2_messages[i])
        print(user1_messages[i])

    if len(user1_messages) > len(user2_messages):
        print('\n'.join([msg for msg in user1_messages[n:]]))
    else:
        print('\n'.join([msg for msg in user2_messages[n:]]))




