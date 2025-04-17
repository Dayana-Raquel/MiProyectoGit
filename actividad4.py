# Imprime un mensaje de bienvenida    
print("¡Hola, bienvenido a tu primer programa en Python!")  

# Pedimos datos al usuario
nombre = input("¿Cómo te llamas?")
edad = int(input("¿Cuántos años tienes? ")) #Convertimos la entrada a número entero

# Mostramos los datos
print("Hola", nombre, "tienes", edad, "años.")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

for i in range(1,11): # del 1 al 10
    resultado = numero *i
    print(numero, "x", i, "=", resultado)

num = -1
while num !=0:
    num = int(input("Escribe un número (0 para salir): "))
    print("Ingresaste:", num)