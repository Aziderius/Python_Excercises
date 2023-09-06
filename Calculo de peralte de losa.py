claro_mas_largo = input("Cuanto mide el lado mas largo de la habitación más amplia de tu proyecto?: (en metros)")

try:
    largo = float(claro_mas_largo)*100
except:
    print("favor de colocar la medida correcta")
    quit()
# h es el valor del peralte neto de la losa
h = largo * ((800 + (0.071*4200)) / 36000)
#print(h)
# r es el valor 3/4 del tamaño de la grava, en este caso se usará grava de 1" de espesor
r = 0.75 * 2.54

peralte_losa = h + r

if peralte_losa > 35:
    print("favor de hacer el calculo para losacero")
    quit()
elif peralte_losa >= 30.0:
    nuevo_peralte_losa = 35
elif peralte_losa >= 25.0:
    nuevo_peralte_losa = 30
elif peralte_losa >= 20:
    nuevo_peralte_losa = 25
elif peralte_losa >= 15.0:
    nuevo_peralte_losa = 20
elif peralte_losa >= 10:
    nuevo_peralte_losa = 15
elif peralte_losa < 9.99:
    print("favor de hacer el calculo para losa maciza")
print("el peralte de la losa será de:", nuevo_peralte_losa, "centimetros")

peralte_frigolit = nuevo_peralte_losa - 5
print("el peralte del frigolit deberá ser de:", peralte_frigolit, "centimetros")
