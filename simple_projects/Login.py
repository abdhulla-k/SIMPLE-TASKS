import time

Username = "AbdhuOmy"
Password = "abcdefgh"

InputUsername = input('Username: ')
InputPassword = input('Password: ')

if InputUsername == Username and InputPassword == Password:
    print('Access granted')
    print('please wait')
    time.sleep(5)                  # for a fun
    print('ok....loading......')
    time.sleep(3)                 # for a fun
    print('.........')
    print('Alright you have security')
elif InputUsername == Username and InputPassword != Username:
    print('wrong password')
elif InputUsername != Username and InputPassword == Password:
    print('wrong username')
else:
    print('you might wanna check both fields...')