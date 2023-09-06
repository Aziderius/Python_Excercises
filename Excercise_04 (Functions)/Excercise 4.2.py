def computepay(a,b):
    if a > 40.0:
        overtime = (a - 40.0) * (b * 0.5)
        pay = a * b + overtime
        return pay
    else:
        regularpay = a * b
        return regularpay
    
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

fhrs = float(hrs)
frate = float(rate)

ttl = computepay(fhrs,frate)
print("Pay: ", ttl)