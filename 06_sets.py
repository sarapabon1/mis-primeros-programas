#Sets - grupo de elementos sin orden, no admite repetidos

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialemnte es un diccionario

my_other_set = {"Sara","Pabon",18}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Pabonsita")
my_other_set.add("Pabonsita") #un set no admite repetidos
print(my_other_set) #un set no es una estructura ordenada

print("Pabone" in my_other_set)#comprobar si existe
print("Pabonsita" in my_other_set)

my_other_set.remove("Sara")
print(my_other_set)

my_other_set.clear() #clear vacia los elementos
print(len(my_other_set))

del my_other_set #del elimina la variable del todo
#print(my_other_set) error

my_set = {"Alex", "Sara", 24}
my_list = list(my_set) #no se conoce el orden de la lista
print(my_list)
print(my_list[0])

my_other_set = {"Python","Java","Html"}

my_new_set = my_set.union(my_other_set).union({"CSS"}) #para unir sets, solo se une no duplica, y tmb se agregan elementos
print(my_new_set)

print(my_new_set.difference(my_set)) #la diferencia de los sets

