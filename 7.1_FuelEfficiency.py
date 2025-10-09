distance = float(input("Enter distance travelled (in kilometers):"))
fuel_consumed = float(input("Enter fuel consumed (in liters):"))
efficiency = distance/fuel_consumed
fuel_efficiency = round(efficiency,2)
print("Fuel Efficiency:", fuel_efficiency, "km/L")