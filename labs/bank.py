# Program to calculate simple interest in a bank

# Input from user
capital = float(input("Enter the capital amount: "))
rate = float(input("Enter the interest rate (%): "))
years = float(input("Enter the number of years: "))

# Calculate interest
interest = (capital * rate * years) / 100

# Display result
print("The calculated interest is:", interest)


