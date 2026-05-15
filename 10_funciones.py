#Funciones, resuelve problemas concretos y se guardan para reutilizar

def my_function (): #funcion simple, sin parametros
    print("Esto es una función")

my_function () #se ejecuta lo que esta en la funcion pq se definio y luego se llamo
my_function ()
my_function ()


def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(15, 22) #si se definieron dos parametros, al llamar la funcion se debe especificar y usar los parametros

sum_two_values(1455, 2222)
sum_two_values("1", "22") #se concatena pq es str
sum_two_values(1.5, 2.2)


def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values_with_return(10, 5) #return guarda los valores en la variable
print(my_result)
   

def print_name (name, surname):
    print(f"{name} {surname}") #para acceder a los valores con {}


print_name(surname ="Pabon" , name = "Sara") #cambio de orden da valores

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Sara" , "Pabon")
print_name_with_default("Sara" , "Pabon" , "Paboncita")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola" , "Saraaa" , "Python")


