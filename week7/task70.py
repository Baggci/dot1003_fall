
def create_coordinates(x, y):
    return (int(x), int(y))

game_table = [['','',''],['','',''],['','','_']]
user_inputs = []
my_flag = True
while my_flag:
    command = input("please type new or exit: ")
    
    if command == "exit":
        my_flag = False  
    elif command == "new":
        val_x = input("please enter x: ")
        val_y = input("please enter y: ")
        
        coord = create_coordinates(val_x, val_y)
         
        user_inputs.append(coord)


for coord in user_inputs:
    x = coord[0]
    y = coord[1]
    game_table[x][y] = '*'

for row in game_table:
  print(*row)