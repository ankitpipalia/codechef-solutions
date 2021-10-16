def checkPrimality(num):
    isprime = 0
    for x in range(2, num-1):
        if num % x == 0:
            isprime = 1
            break

    if isprime:
        print("yes")
    else:
        print("no")


tcase = int(input())

while(tcase):
    num = int(input())
    checkPrimality(num)
    tcase -= 1

