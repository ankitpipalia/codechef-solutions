tcase = int(input())

while(tcase):

    x1, x2 = input().split(" ")

    if(int(x1) > int(x2)):
        print(x1 +" "+str(int(x1) + int(x2)))
    else:
        print(x2 +" "+str(int(x1) + int(x2)))

    tcase -= 1