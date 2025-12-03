age = int(input("How old are you? "))
if age <= 5:
    print("Your Ticket is Free")
elif age > 5 and age <= 12: 
    print("Your Ticket is $5")
elif age >= 13 and age <= 64: 
    print("Your Ticket is $12")
elif age >= 65: 
    print("Your Ticket is $8") 
