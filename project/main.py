try:
    userDb = {
        'alex@gmail': 'alex123',
        '1': '1',
        'oleh@icloud': 'oleh89',
        '2': '2'
    }

    i = 0
    while i < 3:

        checklogin = str(input("login -> "))
        checkpassword = str(input("password -> "))

        if checklogin in userDb and userDb[checklogin] == checkpassword:
            print('registration is successful')
            break
        if i <= 1:
            print('registration is failed, please try again')
        else:
            print('unauthorized access attempt')
        i += 1

except ValueError:
    print('Please, input your correct data')
