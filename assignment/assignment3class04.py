P = float(input("Enter the principal balance: "))
r = float(input("Enter the annual interest rate (in %): ")) / 100
t = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# To Calculate the final amount using compound interest formula
A = P * (1 + r / n) ** (n * t)

# Output
print("The final amount after compound interest is:", A)
