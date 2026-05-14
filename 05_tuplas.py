#tuplas
#almacena elementos y no se modifica, es inmutable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (18, 1.68, "Sara", "Pabon", "Sara")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-6]) indexerror


print(my_tuple.count("Pabon")) #cuenta elementos selecciondos
print(my_tuple.index("Sara")) #dice en que posicion esta ubicado el elemento en la tupla
print(my_tuple.index("Pabon"))

#las tuplas son valores constantes no se puede agregar o quitar datos

my_tuple = list(my_tuple)
print(type(my_tuple)) #para volverlo lista y poder modificar 
del my_tuple #elimina la lista, si es tupla no se puede eliminar
print(my_tuple)

