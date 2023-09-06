fname = input("Enter file name: ")
try:
    open(fname)
except:
    print("File cannot be found:")
    quit()
    
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dictionary = dict()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        #print(words[2])
        emails = words[1]
        dictionary[emails] = dictionary.get(emails,0) + 1
#print(dictionary)

lst = list()
for key, val in list(dictionary.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[0:1]:
    print(key, val)
#print(email,numbers)