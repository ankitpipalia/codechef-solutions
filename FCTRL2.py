tcase = int(input())

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

while(tcase):
    num = int(input())
    print(factorial(num))
    tcase -= 1

