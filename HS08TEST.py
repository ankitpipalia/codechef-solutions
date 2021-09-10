<<<<<<< HEAD
amount, balance = input().split(" ")
amount = float(amount)
balance = float(balance)
charges = float(amount + 0.5)

if amount % 5 == 0 and charges <= balance:
    print("%.2f" %(balance - charges))
else:
=======
amount, balance = input().split(" ")
amount = float(amount)
balance = float(balance)
charges = float(amount + 0.5)

if amount % 5 == 0 and charges <= balance:
    print("%.2f" %(balance - charges))
else:
>>>>>>> 83b4ac685732d66a95a50f86bc7f8eee45be0e28
    print("%.2f" %balance)