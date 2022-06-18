def is_valid_password(password):
    s = psw.split(':')
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    if len(s) != 3:
        flag1 = False
    a = s[0]
    b = int(s[1])
    c = int(s[2])
    if a != a[::-1] or c % 2 != 0:
        flag2 = False
    if b < 2:
        flag3 = False
    for i in range(2, b):
        if b % i == 0:
            flag4 = False
    return flag1 and flag2 and flag3 and flag4

psw = input()

print(is_valid_password(psw))

