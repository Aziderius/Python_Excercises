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
        finddom = emails.find("@")
        domain = emails[finddom+1:]
        #print(domain)
        dictionary[domain] = dictionary.get(domain,0) + 1
print(dictionary)