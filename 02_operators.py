#Operadores
print(3 + 4) #suma
print(3 - 4) #resta
print(3 * 4) #multiplicacion
print(3 / 4) #division
print(10 % 2) #residuo division
print(15 % 4)
print(10 // 3) #resultado numero entero divison
print(2 ** 3) #potencias
print(2 + 4 - 8 * 5) #se pueden combinan todos los signos 

print("Hola " + "python " + "que tal") #solo se suma
#print("hola" + 5) #No se pueden sumar tipos de datos diferente
print("hola " + str(5)) #transformar dato
print("hola " *5 ) 

my_float = 2.5 * 2 #5.0 o sea float no int
print("hola " * int(my_float))

#operadores comparativos

print( 3 > 4) #mayor que
print( 3 < 4) #menor que
print( 3 <= 4) #menor o igual que
print( 3 >= 4) #mayor o igual que
print( 3 == 4) #igual que
print(3 != 4) #diferente que

print( "hola" > "python") #ordenacion alfabetica y mayuscula por ASCII
print( "hola" < "python")
print( "hola" == "hola") 
print("hola" != "python")


#operadores logicos

print(3 > 4 and "hola" > "python") #false y false = false, false y true = false
print(3 > 4 or "hola" > "python") #false o false = false, true y false = true
print(3 < 4 and "hola" < "python")#true y true= true - iguales- igual
print(3 < 4 or "hola" < "python")#false y true= true - diferente true
print(not(3 > 4)) #negar toda la condicion, si es false pone true y al contrario

