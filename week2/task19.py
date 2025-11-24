number = int(input("Please type in a number: "))
if number > 0 and number % 2 == 0:
    print("The number is even ")
elif number > 0 and number % 2 == 1:
    print("The number is odd")   
else:
    print("The number is negative or zero")     