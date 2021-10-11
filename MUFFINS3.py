tcase = int(input())

while(tcase):

    cc = int(input())
    case = int(cc)
    lst = []
    
    while(cc > 1):
        val = case % cc
        lst.append(val)

        cc -= 1

    print((case - max(lst)))

    tcase -= 1