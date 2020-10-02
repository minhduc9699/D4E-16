count = 0
while count < 7:
    username = input('username: ')
    if username == 'd4e':
        password = input('password: ')
        if password == 'd4e':
            print('welcome to d4e')
            break
        else:
            count += 1
            print('quay vao o mat luot r ban ei, nhap lai di')
    else:
        count += 1
        print('quay vao o mat luot r ban eii, nhap lai di')
print('thoi bo di ban ei')