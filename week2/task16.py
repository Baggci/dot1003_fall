valid_communities =[
     "NCR",
     "BROTHERHOOD OF STEEL",
     "CEASAR'S LEGION",
     "GREAT KHANS",
     "VAULT DWELLER"
]
user_input = input("Which community do you belong to?: ")
if user_input.upper() in valid_communities:
    print("You're belong to Fallout Universe.")
else:
    print("Nope, you are not belong to Fallout Lore")    