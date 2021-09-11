tcase = int(input())

def split(num):
    return [digit for digit in num]

while(tcase):
    
    num = str(input())
    lst = []
    lst = split(num)

    print(lst.count("4"))
    
    tcase -= 1