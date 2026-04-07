#Variables

my_string_variable = "holaa"  #lugar que almacena algo 
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) #cambiar tipo de variable
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


#concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) #mostrar datos en cadena
print("Este es el valor de:", my_bool_variable)


#algunas funciones del sistema
print(len(my_string_variable)) #cuenta todos los caracteres

#variables en una sola linea. cuidado con abusar de esta sintasix
name, surname, alias, age = "Sara", "Mendez", "Pabon", 17
print("Me llamo:", name, surname, "Y mi alias es:", alias,"Mi edad es:", age)
 
#inputs, preguntan y almacenan respuesta

firstname = input("cual es tu nombre?")
age = input("cual es tu edad?")
print(firstname)
print(age)
print("Bienvenida", firstname)


#forzamos el tipo
address: str = "Mi direccion"
address = 32
address = 3.4   #toma el ultimo dato
print(type(address))

