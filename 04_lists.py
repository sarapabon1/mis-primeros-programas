#listas - conjunto de elementos con una posicion

my_list = list()
my_other_list = []


print(len(my_list))

my_list = [18, 25, 60, 18, 45]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.70, "Sara", "Pabon"] #se pueden guardar varios tipos de dato

print(type(my_other_list))

print(my_other_list[0]) #se empieza por 0 en lugar de 1
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[5]) #index erorr
print(my_other_list.count("Sara"))
print(my_list.count(18)) #cuenta el numero de veces repetidas un elemento

age, height, name, surname = my_other_list #misma posicion lista
print(name) 

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list) #concatenar listas


my_other_list.append("SaraPab") #append inserta otro elemento al final
print(my_other_list)
    
my_other_list.insert(1, "rojo") #insertar un elemento en cierta posicion
print(my_other_list)

my_other_list[1] = "azul" #modifica el valor seleccionado

my_other_list.remove("azul") #elimina un valor
print(my_other_list)

my_list.remove(18) #elimina un valor
print(my_list)

my_list.pop()
print(my_list) #elimina el ultimo elemento

print(my_list.pop(2)) #elimina el elemento seleccionado
print(my_list)

my_pop_element = my_list.pop(1) #se guarda en la variable el valor elimanado, lo devuelve
print(my_pop_element)
print(my_list)


my_new_list = my_list.copy() #copia los valores de la lista y se guarda en la nueva variable


my_new_list.reverse()#ordena los valores al reves
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list.clear() #borra la lista
print(my_list)
print(my_new_list)

my_list

my_list = "Hola python"
print(my_list)
print(type(my_list)) #tipado dinamico que cambia y se adapta