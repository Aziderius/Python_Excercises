import re
total = 0
handle = open('texto.txt')
number_list = []
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if len (numbers) > 0: 
        for val in numbers:
             number_list.append(int(val))

total = sum(number_list)
print(total)