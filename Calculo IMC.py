peso = input("Cuanto pesas?(en kg)" )
estatura = input("Cuanto mides?(en m)" )

try:
    f_peso = float(peso)
    f_estatura = float(estatura)
except:
    print("Favor de colocar tus datos correctamente (numeros)")
    quit()

imc = f_peso / (f_estatura ** 2)
print(imc)
if imc > 40:
    print("Obesidad grado III.")
elif imc > 35:
    print("Obesidad grado II.")
elif imc > 30.0:
    print("Obesidad grado I.")
elif imc >= 25.0:
    print("Sobrepeso.")
elif imc >= 18.5:
    print("Normal.")
elif imc < 18.49:
    print("Bajo peso.")