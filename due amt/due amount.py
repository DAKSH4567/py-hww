total_bill = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter paid amount: "))

if paid_amount > total_bill:
    print("Paid amount is greater than bill amount")
elif paid_amount == total_bill:
    print("No due amount")
else:
    due_amount = total_bill - paid_amount
    print("Due amount:", due_amount)
