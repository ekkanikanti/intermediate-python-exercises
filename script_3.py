string = input('Enter a string: ')
lower = string.lower()
dict = {}

for x in lower:
    count = 0
    for y in lower:
        if x == y:
            count += 1
    if x not in dict and x.isspace() == False:
        dict.update({x: count})

print(dict)