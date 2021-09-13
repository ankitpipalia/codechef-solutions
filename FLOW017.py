tcase = int(input())

while(tcase):

    lst = []
    a, b, c = map(int, input().split(" "))
    lst.append(a)
    lst.append(b)
    lst.append(c)
    
    lst.sort()

    print(lst[1])
    
    tcase -= 1