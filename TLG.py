tcase = int(input())
name = dict()

while(tcase):
    p1, p2 = map(int, input().split(" "))

    if p1 >= p2:
        name[p1 - p2] = 1
    else :
        name[p2-p1] = 2

    tcase -= 1

x = max(name.keys())

print(name[int(x)] , int(x))