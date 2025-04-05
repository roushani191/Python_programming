email = input('Enter email:')
password = input('Enter password:')

if email == 'rous11@gmail.com' and password == 'rk12':
    print('Welcome')

elif email == 'rous11@gmail.com' and password != 'rk12':
    print('Incorrect password')
    password = input('Enter password again:')

else:
    print('Not valid')    