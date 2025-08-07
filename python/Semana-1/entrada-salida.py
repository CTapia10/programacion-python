# Funcion print para mostrar un mensaje en pantalla
print("Hola como estas?")

# Funcion input
nombre = input("Porfavor, escribe tu nombre: ")

# Utilizamos print para mostrar el nombre que ingreso el usuario
print("Mucho gusto " + nombre + "!")

# Pido edad al usuario
edad = input("Cuantos anios tenes? ")

# Muestro la edad en pantalla
print("Tu edad es de " + edad +" anios")

# Pido numero entero
numero_entero = input("Ingrese un numero entero ")

# Convertimos (Casteamos) el dato ingresado a un numero entero con int()
numero_entero = int(numero_entero)

# Mostramos el numero entero con print
print("El numero ingresado es ", numero_entero)

numero_decimal = input("Ingrese un numero decimal ")

# Convierto el dato ingresado a un numero decimal con float()
numero_decimal = float(numero_decimal)

# Mostramos el numero decimal con print
print("El numero ingresado es ", numero_decimal)

suma= numero_entero + numero_decimal
print("La suma de los numeros es: ", suma)