if __name__ == '__main__':
    unsuccessful_logins = 0
    users = {}
    user_info = input()
    while user_info != 'login':
        username = user_info.split(' -> ')[0]
        password = user_info.split(' -> ')[1]
        users[username] = password
        user_info = input()
    login_attempt = input()

    while login_attempt != 'end':
        username = login_attempt.split(' -> ')[0]
        password = login_attempt.split(' -> ')[1]
        user = (username, password)
        if user not in users.items():
            unsuccessful_logins += 1
            print(f'{username}: login failed')
        else:
            print(f'{username}: logged in successfully')
        login_attempt = input()

    print(f'unsuccessful login attempts: {unsuccessful_logins}')
