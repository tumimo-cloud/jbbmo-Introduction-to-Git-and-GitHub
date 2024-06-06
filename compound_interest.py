# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# compound interest = p * (1 + r/100)^t


# Input:
#    p, principal amount
#    t, time period in years
#    r, annual rate of interest
# Output
#    simple interest = p*t*r

if __name__ == "__main__":
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the time period: "))
    r = float(input("Enter the rate of interest: "))
    simple_interest = p * t * r
    print("The simple interest is {:.2f}", simple_interest)
