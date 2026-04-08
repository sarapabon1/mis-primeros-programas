#strings

my_string = "Mi string"
my_other_string = "mi otro textoo"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\t Este es un string \n escapado"
print(my_scape_string)

#formateo
#permite combinar texto + variable sin concatenar todo
#string %s numero entero %d

name, surname, age = "sara", "pabon", 18

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #forma 1
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #forma 2
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #forma 3, la mejor

#desempaquetado de caracteres
# p y t h o n
# 0 1 2 3 4 5

lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(d)

#division
language_slice = lenguaje[1:3]
print(language_slice)

language_slice = lenguaje[1:]
print(language_slice) #ython

language_slice = lenguaje[-2]
print(language_slice) #o

#reverse

reverse_language = lenguaje[::-1]
print(reverse_language) #invertir palabra

#funciones

print(lenguaje.capitalize()) #primer letra mayuscula
print(lenguaje.upper()) #todo mayuscula
print(lenguaje.count("t")) #cuenta numero letra
print(lenguaje.isnumeric()) #dice si es numero o no
print("1".isnumeric())
print(lenguaje.lower()) #todo minuscula
print(lenguaje.upper().isupper()) #verifica que este en mayuscula
print(lenguaje.startswith("py")) 


