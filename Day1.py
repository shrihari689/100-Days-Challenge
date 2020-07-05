# Write a Python Program to count of each character in the given String followed by the character.
# Sample Input: MMMAAAAIILL
# Smaple Output: 3M3A2I3L


# Input
s = input()

# Not Preserving the Order
print("Not Preserving the Order")
for i in set(s):
    print("{0}{1}".format(s.count(i), i), end="")
print()

# Preserving Order of the String
print("Preserving Order of the String")
index = 0
l = len(s)
while(index < l):
    count = s.count(s[index])
    print("{0}{1}".format(count, s[index]), end="")
    s = s.replace(s[index], '')
    l = l - count
