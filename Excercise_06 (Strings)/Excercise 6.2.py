word = 'el pana antonio'
letter = "a"

def counting(word, letter):
    count = 0
    for strings in word:
        if strings == letter:
            count = count + 1
    return count

respuesta = counting(word, letter)
print(respuesta, letter, "in", word)