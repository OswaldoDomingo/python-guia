# Los operadores de identidad son otro tipo de operadores especiales en Python. Son (is y is not). 
# Estos operadores se utilizan para comprobar si dos variables o valores se encuentran en la misma asignación de memoria.

x1 = 10
y1 = 10
x2 = "Hola"
y2 = "Hola"
x3  = [1,2,3]
y3  = [1,2,3]

print(x1 is not y1) #False
print(x2 is y2) # True
print(x3 is y3) # False

# En este ejercicio, x1 e y1 son variables con valores similares (valor entero 10).
# Esto significa que son iguales e idénticas, al igual que las variables x2 e y2 con valores de cadena similares e iguales. Sin embargo, x3 e y3, aunque iguales, no son idénticas porque son listas y las listas son mutables (esto significa que pueden ser modificarse). El intérprete asigna a las listas memoria separada aunque sean iguales.
# A continuación se muestra una tabla que define lo que hacen los operadores de identidad.
# Operador     Significado 
# is           Devuelve True si los operandos son idénticos.
# is not       Devuelve True si los operandos no son idénticos.

