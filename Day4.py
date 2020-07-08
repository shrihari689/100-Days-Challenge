# rainfall_mi is a string that contains the average number of inches of rainfall
# in Michigan for every month (in inches) with every month separated by comma. Write code to
# compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months.
# In other words, count the numbers of items with values > 3.0

# Sample Input: "1.65,1.46,2.05,3.03,3.35,3.46,2.83,3.23,3.5,2.52,2.8,1.85"
# Sample Output: 5


# Minimal Solution

rainfall_mi = input()
rainfall_values = map(float, rainfall_mi.split(','))
count = 0
for i in rainfall_values:
    if i > 3.0:
        count += 1
print(count)
