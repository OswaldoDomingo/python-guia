# Números
# Los números enteros, de coma flotante y complejos, definidos como int, float y complex
# respectivamente, son las tres clasificaciones de números en Python. 
#Un Número como tipo de datos almacena valores numéricos y es inmutable, lo que significa que cuando el valor
# de la variable, se asigna un nuevo objeto.
# Creación de objetos numéricos
# Los objetos numéricos (variables) se crean cuando se les asignan valores. 
# En el siguiente ejercicio, crearemos tres objetos x, y, y z, cuando les asignemos valores.
# Ejercicio13: Tipo de datos numéricos

x = 7

print("x es de tipo ", type(x))

y = 0.5

print("y es de tipo ", type(y))

z = 1 + 2j

print("Es ", z, " un numero complejo?", isinstance(1+2j,complex))
print("El valor de z es ", z, type(z))

# A diferencia de la mayoría de los lenguajes de programación orientada a objetos, donde la longitud de un entero está limitada, en Python, un entero puede ser de cualquier longitud y sólo está limitado por la memoria disponible en la que se almacena.
# Un float, por otro lado, tiene una precisión de hasta 15 decimales. La diferencia entre un entero y un flotante es un punto decimal. Por ejemplo, en el Ejercicio13,7 es un entero mientras que 7.0 es un número de coma flotante.
# Un float, por otro lado, tiene una precisión de hasta 15 decimales. La diferencia entre un entero y un flotante es un punto decimal. 
# Por ejemplo, en el Ejercicio13, 7 es un entero mientras que 7.0 es un número de coma flotante.
# Los números complejos en Python se escriben en el formato x + yj donde x es la parte real del número e y es la parte real del número. del número e y es la parte imaginaria. Aunque es bueno conocerlos los números complejos no se utilizan mucho cuando se programa en Python.