num1 = int(input("Please type in a temperatures (F): "))
num2 = (num1 -  32) / 1.8
print(f"{num1} degrees Fahrenheit equals {num2} degrees Celsius")
if num2 < 0:
    print("brr! It's cold in here!")