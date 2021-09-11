import math
tcase = int(input())
while(tcase):

    num = int(input())
    lst = []

    while(num / 10 != 0):
        lst.append(num % 10)
        num = math.floor(num / 10)
    
    print(lst[0] + lst[-1])
    tcase -= 1

