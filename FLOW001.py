lines = int(input())

while(lines > 0):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    lines -= 1
    print(a+b)