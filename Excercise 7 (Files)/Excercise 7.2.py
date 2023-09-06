# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0

try:
    fh = open(fname)
except:
    print("File Cannot be oppened: ", fname)
    quit()
    
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    findnum = line.find(":")
    convnum = line[findnum+1:]
    floatnum = float(convnum)
    # print(floatnum) 
    total = total + floatnum
    count = count+1 
    promedio = total/count 
print("Average spam confidence:", promedio)