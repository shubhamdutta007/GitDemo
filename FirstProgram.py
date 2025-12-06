
P = float(input("Enter the Principle amount "))
R = float(input("Enter the Rate of interest "))
T = float(input("Enter the Time "))

A= P*((1+(R/100)))**T
A1= P*pow((1+R/100),T)

CI=A-P
CI1=A1-P

print("COMPOUND INTEREST is:", round(CI, 2))
print("COMPOUND INTEREST is:", round(CI1, 2))



git pull origin main



