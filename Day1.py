# Write a Python Program to count of each character in the given String and print it followed by the character.
# Sample Input: MMMAAAAIILL
# Sample Output: 3M3A2I3L


# Input
s = input()

# Not Preserving the Order
print("Not Preserving the Order")
for i in set(s):
    print("{0}{1}".format(s.count(i), i), end="")
print()

# Using Dictionaries
print("Using Dictionaries")
b = {}
for i in s:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)


# Preserving Order of the String
print("Preserving Order of the String")
index = 0
l = len(s)
while(index < l):
    count = s.count(s[index])
    print("{0}{1}".format(count, s[index]), end="")
    s = s.replace(s[index], '')
    l = l - count
