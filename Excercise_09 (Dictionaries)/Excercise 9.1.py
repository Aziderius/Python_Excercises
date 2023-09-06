fhand = open('words.txt')
dictionary = dict()
for line in fhand:
    words = line.split()
    #print (line)
    for word in words:
        dictionary[word] = [""]
print(dictionary)