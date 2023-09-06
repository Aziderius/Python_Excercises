fhand = open('romeo.txt')
lst = list()
for line in fhand:
    words = line.rstrip()
    words = line.split()
    if len(words) < 3 :
        continue
    for w in words:
        if words not in lst:
            lst.append(w)
        lst.sort()
print(lst)