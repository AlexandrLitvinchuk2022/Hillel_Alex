enter1 = input("Enter word1: ") # AAAaaaavrnthnrt012399999999
enter2 = input("Enter word1: ") # AAAaaaavrnthnrt5665erjgre012378
set1 = set(enter1)
set2 = set(enter2)
print(f'{set1}')
print(f'{set2}')

#intersection = set1.intersection(set2)
#print(f'set1 & set2 --> {set1 & set2}')

difference = set1.difference(set2)
print(f'set1 - set2 --> {set1 - set2}')
#############################################################
a = 60
b = 13
c = a|b
d = a^b
e = c&b

print(bin(a))
print(bin(b))
print(bin(c))
print(a&b)
print(c)
print(b)
print(d)
print(bin(d))
print(e)

##########################################
read = 1
write = 2
execute = 4

guest = read
user = read | write
admin = read | write | execute



admin = read | write | execute
pedro = admin
print(pedro & read)
print(pedro & write)
print(pedro & execute)