# Write a Python Program to give string as input in the following format (Alphabet followed by the Digit).
# Based on the input, your code should display the result as shown in the below output format.
# Sample Input: N4A2V3E2
# Sample Output: NNNNAAVVVEE


# Input
s = input()


# Minimal Solution
result = ""
for i in range(1, len(s)+1, 2):
    result += (int(s[i]) * s[i-1])
print(result)
