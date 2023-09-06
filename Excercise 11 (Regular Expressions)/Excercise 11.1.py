import re
fname = input("Enter file name: ")
try:
    open(fname)
except:
    print("File cannot be found:")
    quit()
    
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
lst = []

for line in fh:
    line = line.rstrip()
    number = re.findall("^New.* ([0-9]+)", line)
    if len(number) > 0:
        lst += number
        continue
sum, count = 0,0
for val in lst: 
    sum += int(val)
    count += 1
average = int(sum/count)
print(average)