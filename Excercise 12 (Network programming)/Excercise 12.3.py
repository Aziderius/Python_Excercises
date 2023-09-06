import urllib.request, urllib.parse, urllib.error

url = input("enter a URL: ")

#variables
count = 0
displaycount = 0
charlimit = 3000

try:
    fhand = urllib.request.urlopen(url)
except:
    print("Enter the URL in propet format")
    quit()

for line in fhand:
    line = line.decode().strip()
    count += len(line)
    if displaycount < charlimit:
        displaycount += len(line)
        if not displaycount > charlimit:
            print(line)
        else:
            displayEnds = (charlimit - displaycount) + 1
            displaycount = displaycount - (displaycount - charlimit)
            print(line[:displayEnds])
    #print(line)
print(f"\nDisplay ends at character count of", displaycount)
print(f"total number of characters in this page", count)