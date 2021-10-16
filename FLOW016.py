tcase = int(input())

while(tcase):

    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    lst = []

    if(num1 < num2):
        for x in range(1,num1):
            if(num1 % x == 0 and num2 % x == 0):
                lst.append(x)
    
    elif(num1 > num2):
        for x in range(1,num2):
            if(num1 % x == 0 and num2 % x == 0):
                lst.append(x)
    
    elif(num1 == num2):
        lst.append(num1)

    lst1 = {}
    lst1 = set()

    for x in range(1,num1+1):
        t1 = num1 / x
        t1_int = t1.is_integer()
        if(t1_int):
            num1 = num1 / x
            lst1.add(x)


    for x in range(1,num2+1):
        t1 = num2 / x
        t1_int = t1.is_integer()
        if(t1_int):
            num2 = num2 / x
            lst1.add(x)
    
    multi = 1
    for y in lst1:
        multi = multi * int(y)

    print(str(max(lst))+" "+str(multi))

    tcase -= 1     
