snum = int(input())

ecount = 0
ocount = 0

x = input()
lst = x.split(" ") 
for ele in lst:
    if(int(ele) % 2 == 0):
        ecount += 1
    else:
        ocount += 1

if(ecount > ocount):
    print("READY FOR BATTLE")
else:
    print("NOT READY")