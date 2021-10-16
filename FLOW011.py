tcase = int(input())
while(tcase):
    gsalary = 0.0

    bsalary = int(input())

    if(bsalary < 1500):
        gsalary = 2 * bsalary

    elif(bsalary > 1500):
        gsalary = 500 + (0.98 * bsalary) + bsalary

    print("%.2f" %gsalary)

    tcase -= 1