distance_travelled =  float(input("How far have you travlled: "))
fuel_used =  float(input("How much fuel have you used: "))
price =  float(input("How much is the fuel: "))

trip_cost = (distance_travelled * price) /fuel_used 

print("You total trip cost is:$" + str(round(trip_cost, 3)))




