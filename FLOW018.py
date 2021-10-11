def fact(y):
    if(y > 1):
        return (y*fact(y-1))
    else:
        return 1

tcase = int(input())
while(tcase):
    y = int(input())
    print(fact(y))
    tcase-=1