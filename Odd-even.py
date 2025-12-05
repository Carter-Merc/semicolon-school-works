integer_numbers = int(input("Enter an amount of integers: "))

print("Enter an Int:")

counter = 1
oddTotal = 0
evenTotal = 0



while counter <= integer_numbers: 
        
    number = int(input())
    
    if (number%2 == 0): 
        evenTotal += number
    else: 
        oddTotal += number  
    counter = counter + 1
    print("The total of Odd numbers and sum total numbers are", oddTotal, "and", evenTotal)
