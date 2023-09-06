word = 'asldkfnasñdkfjasñdkjasjkfdsfa'
dictionary = dict()

for letter in word:
    dictionary[letter] = dictionary.get(letter,0) + 1
print(dictionary)

lst = list(dictionary.keys())    
lst.sort()
for key in lst:
    print(key, dictionary[key]) 

