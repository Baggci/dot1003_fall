number = 3
password = 1881
my_flag = True

while my_flag:
    user_password = int(input("Password: "))
    number = number - 1
    if password == user_password:
        print("Welcome")
        my_flag = False
    elif number == 0:
        print("Incorrect Password. Exterminate...")
        my_flag = False
    elif password != user_password :
        print("Try again")       
