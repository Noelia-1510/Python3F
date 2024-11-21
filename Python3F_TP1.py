# 1)Realizar un programa que le pida al usuario su nombre y lo escriba en mayúsculas.

nombre = input("Ingrese su nombre: ")
print("su nombre es : "+nombre.upper())

# 2) Realizar un programa que le pida al usuario un número y le sume 5, el resultado debe mostrarse por pantalla.

numero = int(input("Ingrese un numero: "))
numero += 5
print("La suma es : ", numero)

# 3) Realizar un programa que le pida al usuario su nombre y apellido , mostrarlos en un mensaje de bienvenida por la pantalla.

nombre = input("Inrese su nombre: ")
apellido = input("Inrese su apellido: ")
print("Bienvenido!", nombre,apellido)

# 4) Ingresar 5 números y calcular su promedio , el resultado mostrarlo por pantalla.

num1 = float(input("Ingrese un primer numero: "))
num2 = float(input("Ingrese un segundo numero: "))
num3 = float(input("Ingrese un tercer numero: "))
num4 = float(input("Ingrese un cuarto numero: "))
num5 = float(input("Ingrese un quinto numero: "))

promedio = num1 + num2 + num3 + num4 + num5 / 5

print("El promedio es: ", promedio)

# 5) Realizar un programa que muestre cualquier frase ingresada por el usuario en minúscula.

frase = input("Ingrese una frase: ")
print("La frase ingresada es: "+frase.lower())