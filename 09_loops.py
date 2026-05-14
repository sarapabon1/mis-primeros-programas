
#LOOPS, bucles, ciclos sirve para pasar por el mismo codigo varias veces


#While, se pasa una condicion, mientras sea verdadero hace algo


my_condition = 0



 #si la condicion no cambia el bucle es infinito
while my_condition < 10:
    print(my_condition)
    my_condition += 2

else:
    print("Mi condición es mayor o igual que 10")

print("La ejecucion continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la condicion")
        break

    print(my_condition) 
#el break detiene la ejecucion
print("La ejecucion continua")

# For, cumple una condidcion, sirve para iterar un listado de elementos

my_list = [35, 24, 62, 52, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.68, "Sara", "Pabon")

for element in my_tuple:
    print(element)

my_set = {"Sara","Pabon", 18}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Sara", "Apellido":"Pabon", "Edad":18, 1:"Python"} 

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")

else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecucion continua")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")

else:
    print("El bucle for ha finalizado")

#continue sigue corriendo el bucle pero vuelve al for







