sum = 0
count = 0
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        count += 1
        sum = sum + number
    except:
        print("Invalid input")
        continue
    
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

print("sum:", sum, "count:", count, "average:", sum/count)
print("largest:", largest, "smallest:", smallest)