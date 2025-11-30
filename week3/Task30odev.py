print("Dumb calcul.1 If you want to exit, enter 0")

my_flag = True

total_number = 0
number1 = 0
odd = 0
even = 0

while my_flag:
    number = int(input("please enter a number: "))
    if number == 0:
        my_flag = False
        mean = number1 / total_number
        print(f"Total Number: {total_number}")
        print(f"Sum: {number1}")
        print(f"Mean: {mean}")
        print(F"Odd: {odd}, Even: {even}")
    else:
        number1 = number1 + number
        total_number = total_number + 1 
        if number % 2 == 0:
            even = even + 1 
        else:
            odd = odd + 1

print("bitti")