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

email = None
numbers = None
for number, count in dictionary.items():
    if numbers is None or count > numbers:
        numbers = count
        email = number
print(email,numbers)