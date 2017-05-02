num = 0

while num < 5:
    id = input('id: ')
    password = input('password: ')
    if id == 'jonnythebard':
        if password == '123':
            print('welcome,', id)
            break
        else:
            print('wrong password. you have', str(4 - num), 'chances.')
    else:
        print('id', id, 'does not exist.', 'you have', str(4 - num), 'chances.')
    num += 1
