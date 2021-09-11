import math
tcase = int(input())

while(tcase):
    num = int(input())
    sum = 0
    while(num / 10 != 0):
        sum = sum + (num % 10)
        num = math.floor(num / 10)
    print(int(sum)) 
    tcase -= 1