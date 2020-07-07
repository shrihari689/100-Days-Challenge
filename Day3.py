# Find the total numbers of occurrences of a character in the string and caluclate the summation of all total occurrances.
# SAMPLE INPUT: abxylaclybb
# SAMPLE OUTPUT: 11


# Input

s = input()

# Minimal Solution
print("Minimal Solution:", len(s))

# Obeying the Question
letters = {}
for i in s:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
print("Obeying the Question:", sum(letters.values()))
