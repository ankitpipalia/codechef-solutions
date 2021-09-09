n, divider = input().split(" ")
n = int(n)
divider = int(divider)
counter = 0

while(n > 0):
    n -= 1
    value = int(input())
    if value % divider == 0:
        counter += 1

print(counter)