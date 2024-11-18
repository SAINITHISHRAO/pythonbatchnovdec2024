#Inputs
#simple interest: A=P(1+rt)
#A = final amount
#P = initial principal balance
#r = annual interest rate
#t = time(in years)
P = float(input("Enter the principal balance: "))
r = float(input("Enter the annual interest rate: ")) / 100
t = float(input("Enter the time in years: "))

# Calculate the final amount
A = P * (1 + t * r)

# Output the result
print("The final amount after interest is:", A)