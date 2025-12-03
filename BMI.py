weight = float(input("What is your weight: "))
height = float(input("How tall are you: "))
bmi = (weight * height)/height

if bmi < 18.5: 
   print("Underweight")
elif bmi <= 24.9: 
   print("Normally")
elif bmi <= 29.9: 
   ("Overweight") 
elif bmi >= 30: 
   print("obese")
