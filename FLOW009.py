tcase = int(input())
sum = 0.00
x = 0.0

while(tcase):
    n1, n2 = input().split(" ")
    n1 = int(n1)
    n2 = int(n2)

    if (n1 < 1000):
        sum = float(n1) * float(n2)
    elif(n1 > 1000):
        sum = float(n1) * float(n2)
        x = sum / 10
        sum = sum - x

    print("%.6f" %sum)
    tcase -= 1