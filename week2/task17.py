user_point = int(input("How many points [0-100]: "))

if user_point >= 50 and user_point <=100 :
    print("Grade: pass")
elif user_point < 50 and user_point >=0:
    print("Grade: fail") 
elif user_point > 100:
    print('Impossible!')      
else:
    print("Grade: you what? ")    