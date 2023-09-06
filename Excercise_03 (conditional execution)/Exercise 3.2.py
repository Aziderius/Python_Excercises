hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fhrs = float(hrs)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fhrs > 40.0:
    overtime = (fhrs - 40.0) * (frate * 0.5)
    pay = fhrs * frate + overtime
    print("Pay:", pay)
else:
    regularpay = fhrs * frate
    print("Pay: ", regularpay)