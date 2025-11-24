times = int(input("How many times a week do you eat at the student cafeteria? "))
price = int(input("The price of a typical student lunch? "))
other = int(input("how do you spend on groceries in a week? "))
 
weekly_total = times * price *other
daily = weekly_total / 7
montly = weekly_total * 4.33

print("aveage food expenditure: ")
print("daily:", daily, "liras" )
print("weekly:", weekly_total, "liras")
print("montly", montly, "liras")                                          