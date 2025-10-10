#Define function for delivery fee
def calc_delivery_fee(distance, rate):
    fee = distance*rate
    total_fee = round(fee,2)
    return total_fee

#Ask for distance and rate
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

#Calculate delivery fee
total_fee = calc_delivery_fee(distance, rate)

print(f"Total Delivery Fee: ₱", total_fee)
