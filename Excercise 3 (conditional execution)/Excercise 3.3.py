score = input("Enter score: ")

try:
    fscore = float(score)
except:
    print("Bad score")
    quit()

if fscore > 1:
    print("Bad Score")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
elif fscore > 0.6:
    print("F")