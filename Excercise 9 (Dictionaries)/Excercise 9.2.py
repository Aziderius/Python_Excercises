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
        days = words[2]
        dictionary[days] = dictionary.get(days,0) + 1
print(dictionary)