# Introduction to Git and GitHub

## Simple Interest Calculator

This is a calculator that computes simple interest given the principal amount, the annual rate of interest, and the time period in years.

### Formula
The simple interest \( SI \) is calculated using the formula:

\[ SI = \frac{P \times R \times T}{100} \]

where:
- \( P \) is the principal amount
- \( R \) is the annual rate of interest
- \( T \) is the time period in years

### Python Example
Below is a simple Python function to calculate the simple interest:

```python
def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

# Example usage
principal = 1000  # Example principal amount
rate_of_interest = 5  # Annual rate of interest in percentage
time_in_years = 3  # Time period in years

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate_of_interest, time_in_years)
print(f"Simple Interest: {simple_interest}")
