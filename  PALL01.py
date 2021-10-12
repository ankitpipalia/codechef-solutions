tcase = int(input())

while(tcase):
    num = input()
    if(num[0] == 0):
        continue
    else:
        x = num[::-1]
        if(x == num):
            print("wins")
        else:
            print("loses")
    tcase -= 1