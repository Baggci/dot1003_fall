hourly_wage = float(input("Hourly wage : "))
hours_worked = int(input("Hours workde : "))
day_off = input("Day of the week : ")
daily_wages = hourly_wage * hours_worked 

if day_off == "sunday" :
    daily_wages = daily_wages * 2


print(f"Daily_wages : {daily_wages} liras")