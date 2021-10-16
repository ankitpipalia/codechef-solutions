tcase = int(input())

while(tcase):

    char = input()

    if(char == 'b' or char == 'B'):
        print("BattleShip")
    
    elif(char == 'c' or char == 'C'):
        print("Cruiser")
    
    elif(char == 'd' or char == 'D'):
        print("Destroyer")

    elif(char == 'f' or char =='F'):
        print("Frigate")

    tcase -= 1