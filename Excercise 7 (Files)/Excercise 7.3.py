fhand = input("Enter file name: ")

try:
    fh = open(fhand)
    count = 0
    total = 0

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
    if fh == "na na boo boo":
        print("FUCK YOU NIGGA, I CATCH YOU!")
        quit()
except: 
    print("File not found, please try again")
    quit()