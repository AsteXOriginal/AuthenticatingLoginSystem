password = 1432

i = 0
while i < 3:
    checkpassword = int(input("password -> "))
    if checkpassword == password:
        print('registration is successful')
        break
    if i <= 1: 
        print('registration is failed, please try again')
   
    else:
        print('unauthorized access attempt')
    i += 1