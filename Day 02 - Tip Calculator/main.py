print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? "))
tip_percent = int(input("How much tip would you like to give ? 10, 12, or 15 ?"))
bill_tip = bill * tip_percent / 100 + bill
split = input("How many people to split the bill up ? ")
split_bill = bill_tip / int(split)
print(f"Each person should pay : {(round(split_bill,2))}")

