# 1)Realizar un programa que me diga si un numero es par o impar.

numero = int(input ("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero es par ")
else:
    print("El numero es impar ")

# 2)Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10).

numero = int(input("Ingrese un numero: "))
print("Tabla de multiplicar del: ",numero)

for tabla in range(1,11):
    resultado = numero * tabla
    print(numero ,"x", tabla , "=", resultado)
    
# 3)Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >=18:
    print("Es mayor de edad puede ingresar ")
else:
    edad < 18
    print("Es menor de edad no puede ingresar ")
    
# 4)Realizar un programa donde el usuario ingrese una palabra y un numero e imprima por pantalla la palabra ingresa tantas veces como el numero ingresado.

palabra = input("Ingrese algo: ")
numero = int(input("Cuantas veces queres que se repita? "))
contador = 0

while contador <= numero:
    contador += 1
    print(palabra)
    
# 5)Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla.

suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un número (0 para terminar): "))
    suma += numero

print("La suma total es:", suma)
