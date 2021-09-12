count = int(input())
lst = []

while(count):
    lst.append(int(input()))
    count -= 1
    
lst.sort()

for x in lst:
    print(x)