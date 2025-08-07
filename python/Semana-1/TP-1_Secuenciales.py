## Trabajo practico 1 - Secuenciales 
#  Cristian Tapia - 2025

# Ejercicio 1
print("Hola Mundo!")


# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")


# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido} tengo {edad} anios y vivo en {pais}")


# Ejercicio 4
# Calculo del area de un circulo
radio = float(input("Ingrese el radio de un circulo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
# Impresion del resultado
print("El area del circulo es:", area)
print("El perimetro del circulo es:", perimetro)


# Ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = segundos / 60
horas = minutos / 60
print(f"La cantidad de horas respecto a los segundos ingresados es de: {horas}")


# Ejercicio 6
num = int(input("Ingrese un numero: "))
print(1*num)
print(2*num)
print(3*num)
print(4*num)
print(5*num)
print(6*num)
print(7*num)
print(8*num)
print(9*num)
print(10*num)


# Ejercicio 7
num1 = int(input("Ingrese un numero distinto a 0: "))
num2 = int(input("Ingrese otro numero distinto a 0: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)


# Ejercicio 8
altura = float(input("Ingrese su altura en metros (por ejemplo: 1.65): "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura * altura)
print(f"Su indice de masa corporal es de: {imc} ")


# Ejercicio 9
celcius = float(input("Ingrese una temperatura en grados celcius: "))
fahrenheit = (9/5) * celcius + 32
print(f"La conversion a grados fahrenheit: {fahrenheit} ")


# Ejercicio 10
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))
print((num1+num2+num3)/3)