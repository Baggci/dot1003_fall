input("Enter your password: ")

my_flag = True

while my_flag:
    password = input("Enter again: ")

    if password != "myPassword":
          print("They are not same: ")
    else:
        my_flag = False
        print("Your password matches and account created successfully")