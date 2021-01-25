'''
Author = Biju
Date = 2021/01/08
Title = Simple password secure
'''
SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('b', '#'), ('r', '%'), ('h', '<'), ('p', '~'), ('v', '+'), ('c', '*'), ('t', '/'), ('g', '='), ('b', '?') ,('S', '$'), ('And', '&'), ('A', '@'), ('O', '0'), ('I', '1'), ('R', '%'), ('H', '<'), ('P', '~'), ('V', '+'), ('C', '*'), ('T', '/'), ('G', '='), ('B', '?'), ('u', '^'))
def secure_Password(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password


if __name__ == '__main__':
    password = input("Enter your password:")
    password = secure_Password(password)
    print(f"Your Secure password is {password}")