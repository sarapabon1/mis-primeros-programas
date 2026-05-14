#condicionales, flujos de ejecucion de codigo, si se cumple la accion descrita se ejecuta el comdicional

my_condition = False


if my_condition: 
    print("Se ejecuta la condición del if")

my_condition = 5 * 5


if my_condition == 10:
    print("Se ejecuta la condición del segundo if") #se ejecuta si es verdadero

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")

else:

     print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

#el else se cumple si no se cumple la condicion if entonces se pide otra cosa, debe haber una respuesta si o si
#elif es para especificar otra opcion que se puede cumplir




print("La ejecución continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena":
    print("Mi cadena de texto no es vacia")

if my_string == "Mi cadena":
    print("Estas cadenas de texto coinciden")
