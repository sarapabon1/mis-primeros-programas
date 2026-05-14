#Diccionarios, estructura para relacionar datos
#Relacion clave - valor

my_dict = dict()
my_other_dict ={}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Sara", "Apellido":"Pabon", "Edad":18, 1:"Python"} 

my_dict = {
    "Nombre":"Sara",
    "Apellido":"Pabon",
    "Edad":18, 
    "Lenguajes":{"Python", "Html", "CSS"},
    1:1.68 
   }  #clave string y valor set

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(my_dict["Nombre"]) #accede al elemento

my_dict["Nombre"] = "Alex"
print(my_dict["Nombre"]) #forma de actualizar la clave

print(my_dict[1])

my_dict["Calle"] = "Calle Sara" #para agregar otro campo
print(my_dict)

del my_dict["Calle"] #elimina el elemento
print(my_dict)

print("Pabon" in my_dict)
print("Nombre" in my_dict) #verifica la clave no el valor

print(my_dict.items()) #muestra listado de items
print(my_dict.keys()) #muestra listado de claves
print(my_dict.values()) #muestra listado de valores


my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, "Pabon")
print((my_new_dict))



