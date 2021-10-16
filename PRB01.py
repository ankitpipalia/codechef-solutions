tcase = int(input())

while(tcase):

    num = int(input())
    flag = 0
    
    for x in range(2,num-1):
        if(num % x == 0):
            flag = 1
    
    if (flag == 1):
        print("no")
    else:
        print("yes")



    tcase -= 1