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
    if line.startswith("From "):
        words = line.split()
        #print(words[2])
        hours = words[5]
        hoursplit = hours.split(":")
        hour = hoursplit[0]
        dictionary[hour] = dictionary.get(hour,0) + 1
print(dictionary)

lst = list()
for key, val in list(dictionary.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)