import numpy as np 
from scipy.stats import chi2_contingency

# data: bill amounts and electricity consumed for 12 months

bill_amounts = [193, 82, 502, 666, 2471, 1567, 1696, 2766, 846, 860, 572, 208] 
electricity_consumed = [51, 221,95,65,379, 226, 293, 376, 72, 137,40, 45]

# Create a contingency table

observed = np.array([bill_amounts, electricity_consumed])

# Perform Chi-Square test

chi2, p, dof, expected = chi2_contingency(observed)

# Set significance level

alpha = 0.05

# Print the results

print(f"Chi-Square Statistic: {chi2}") 
print(f"P-value: {p}") 
print(f"Degrees of Freedom: {dof}") 
print("Contingency Table (Expected values):") 
print(expected)

# Interpret the results

if p < alpha:
    print("Reject the null hypothesis: Electricity consumed is not the same every month.") 
else:
    print("Fail to reject the null hypothesis: There is no evidence to suggest that electricity consumed varies monthly.")