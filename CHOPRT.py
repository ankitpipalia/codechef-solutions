tcase = int(input())

while(tcase):
    n1, n2 = input().split(" ")
    n1 = int(n1)
    n2 = int(n2)

    if (n1 > n2):
        print(">")
    elif (n1 == n2):
        print("=")
    else:
        print("<")
        
    tcase -= 1