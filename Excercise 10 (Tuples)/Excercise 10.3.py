fname = input("Enter file name: ")
try:
    open(fname)
except:
    print("File cannot be found:")
    quit()
    
if len(fname) < 1:
    fname = "mbox-short.txt"

import string
fh = open(fname)
dictionary = dict()
for line in fh:
    line = line.translate(str.maketrans('', '', string.punctuation+'0123456789 \t\n\r')).lower()
    for letter in line:
        dictionary[letter] = dictionary.get(letter, 0) + 1
#print(dictionary)

lst = list()
for key, val in list(dictionary.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)