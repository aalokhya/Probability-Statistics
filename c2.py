import numpy as np

bill_amounts = np.array([193, 82, 502, 666, 2471, 1567, 1696, 2766, 
846, 860, 572, 208]) 
units_consumed = np.array([51, 221, 95, 65, 379, 226, 293, 376, 72, 
137, 40, 45])

# Calculate the mean of bill amounts and units consumed

mean_bill = np.mean(bill_amounts) 
mean_units = np.mean(units_consumed)

# Calculate the differences and products needed for slope calculation

diff_bill = bill_amounts - mean_bill 
diff_units = units_consumed - mean_units

# Slope calculation

slope = np.sum(diff_bill * diff_units) / np.sum(diff_bill**2)

# Intercept calculation using the slope and mean values

intercept = mean_units - (slope * mean_bill)

# Print the equation of the line

print(f"The linear equation is: y = {intercept:.2f} + {slope:.3f}x")