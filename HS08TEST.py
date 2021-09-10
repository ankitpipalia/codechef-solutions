amount, balance = input().split(" ")
amount = float(amount)
balance = float(balance)
charges = float(amount + 0.5)

if amount % 5 == 0 and charges <= balance:
    print("%.2f" %(balance - charges))
else:
    print("%.2f" %balance)