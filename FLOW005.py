import math
tcase = int(input())

while(tcase):
    
    count = 0

    num = int(input())
    
    if(num >= 100):
        val = num/100
        num = num % 100
        count += math.floor(val)

    if(num >= 50):
        val = num/50
        num = num % 50
        count += math.floor(val)

    if(num >= 10):
        val = num/10
        num = num % 10
        count += math.floor(val)

    if(num >= 5):
        val = num/5
        num = num % 5
        count += math.floor(val)
    
    if(num >= 2):
        val = num/2
        num = num % 2
        count += math.floor(val)
    
    if(num >= 1):
        val = num/1
        num = num % 1
        count += math.floor(val)
    
    print(count)
    tcase -= 1
