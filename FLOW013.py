tcase = int(input())

while(tcase):

    x1, x2, x3 = input().split(" ")
    case = int(x1) + int(x2) + int(x3)

    if(case == 180):
        print("YES")
    else:
        print("NO")

    tcase -= 1
