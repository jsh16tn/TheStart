bill = input("What is your bill amount? $")
tip_percent = input("How much do you want to tip in percent? ")

tip = float(tip_percent)/100 * float(bill)

print("Your tip is $" + str(tip))

print("Your total payment is $" + str(tip+float(bill)))