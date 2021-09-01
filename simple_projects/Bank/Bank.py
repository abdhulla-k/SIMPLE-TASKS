class main:
    UserName = 'Abdhu'
    Password = 'abcdefgh'

    def Login(self):
        UserName = input('Enter'+'\n'+'username: ')
        Password = input('Password: ')
        if UserName == self.UserName and Password == self.Password:
                print('Welcome to Bank'+'\n'+'Login completed')
        else:
            print('wrong Username or Password')
        

def Bank(Userinpu):
    print(UserInput)
    x = main()
    x.Login()


if __name__=='__main__':
    UserInput = input('Enter'+'\n'+'1 for Login')
    Bank(UserInput)