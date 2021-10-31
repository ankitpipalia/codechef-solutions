tcase = int(input())

while(tcase):

    lenth = int(input())
    arr = []
    num = input()
    temp = []
    diff = 0

    for x in num.split(" "):
        x = int(x)
        arr.append(x)

    arr.sort()

    for x in range(0,lenth-1):
        if x < lenth:
            diff = arr[x+1] - arr[x]
            temp.append(diff)
        else:
            break
    
    temp.sort()
    lot = len(temp)

    for x in range(0,x):
        if(temp[x] > 0):
            diff = temp[x]
            break

    print(diff)
    tcase -= 1