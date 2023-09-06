list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def middle(t):
    return t[1:-1]
list2 = middle(list)
print(list2)

def chop(t):
    del t[0]
    t.pop()
t2 = chop(list)
print(t2)