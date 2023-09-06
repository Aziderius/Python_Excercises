numlist = list()
while True:
    numbers = input("Enter a number: ")
    if numbers == "done":
        break
    value = float(numbers)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Maximum: ", max(numlist))
print("Minimum: ", min(numlist))
print("Sum: ", sum(numlist))
print("Count: ", len(numlist))
print("Average: ", average)