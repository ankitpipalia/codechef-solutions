tcase = int(input())

while(tcase):
    c1, c2 = input().split(" ")
    c1 = int(c1)
    c2 = int(c2)
    print(c1 % c2)

    tcase -= 1