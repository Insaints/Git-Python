def is_valid_password(password):
    password = password.split(':')
    return (password[0] == password[0][::-1]) and \
    (len([i for i in range(1, int(password[1])+1) if int(password[1]) % i == 0]) == 2) and \
    (int(password[2]) % 2 == 0)

psw = input()


print(is_valid_password(psw))