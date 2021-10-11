tcase = int(input())

menu = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

while(tcase):
    count = 0
    num = int(input())
    lst = menu.copy()
    lst.sort(reverse=True)
    while(num > 0):
        if num>=lst[0]:
            num = num - lst[0]
            count+=1
        else:
            lst.remove(lst[0])
    print(count)

    tcase -= 1