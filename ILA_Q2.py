distance = float(input("Enter distance in kilometers:"))
rate = float(input("Enter rate per kilometer (₱):"))
fee = distance*rate
total_fee = round(fee,2)
print("Total Delivery Fee: ₱", total_fee)