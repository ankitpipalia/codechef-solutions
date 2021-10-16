tcase = int(input())

while(tcase):
    n1, n2 = input().split(" ")
    n1 = int(n1)
    n2 = int(n2)

    while(n1):
        sum = 0
        while(n2):
            sum = sum + n2
            n2 -= 1

        n2 = sum
        n1 -= 1
    
    print(n2)

    tcase -= 1  
