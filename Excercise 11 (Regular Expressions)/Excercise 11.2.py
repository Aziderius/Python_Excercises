import re

#Get file
try:
    email_file = open(input('Enter file:'))
except:
    print('Invalid file')
    exit()

#Extract all the numbers
revision_number_list = []
for line in email_file:
    revision_number = re.findall('New Revision: ([0-9]+)', line)
    if len(revision_number) > 0:
        revision_number_list += revision_number

#Find the average
sum, count = 0,0
for number in revision_number_list:
    sum += int(number)
    count += 1
avg = int(sum/count)
print(avg)