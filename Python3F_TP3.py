# 1)Cree una funcion que calcule el promedio de N notas.

def calcular_promedio():
    suma = 0
    cantidad_notas = int(input("¿Cuantas notas queres ingresar? "))
    
    for N in range(cantidad_notas):
        notas = float(input(f"Ingrese la nota {N+1}: "))
        suma += notas
    
    promedio = suma / cantidad_notas
    return promedio

promedio = calcular_promedio()
print(f"El promedio es: {promedio}")

# 2)Cree una funcion que determine si un color es primario o no, se debe imprimir por pantalla la leyenda “el color X es primario “ o “el color X no es primario”.

def es_color_primario(color):
    if color == 'rojo' or color == 'azul' or color == 'amarillo':
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")

color = input("Ingrese un color: ")
es_color_primario(color)

# 3)Cree una funcion que determine que numero de una serie de N numeros es mayor.

def numero_mayor():
    cantidad = int(input("¿Cuantos numeros queres ingresar?: "))
    if cantidad <= 0:
        print("La cantidad de numeros debe ser mayor que cero")
    
    mayor = float(input("Ingresa el primer numero: "))
    
    for N in range(1, cantidad):
        numero = float(input(f"Ingresa el numero {N+1}: "))
        if numero > mayor:
            mayor = numero
    
    print(f"El número mayor es: {mayor}")

numero_mayor()

# 4)Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario.

def dibujar_rectangulo(filas, columnas):
    for i in range (filas):
        print("*" * columnas)

filas = int(input("Ingrese la cantidad de filas del rectangulo: "))
columnas = int(input("Ingrese la cantidad de comunas del rectangulo: "))

dibujar_rectangulo(filas, columnas)

# 5)Cree una funcion que calcule el Factorial de un numero entero positivo.

def calcular_factorial(n):
    if n < 0:
        return 
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

numero = int(input("Ingrese un numero entero positivo: "))

resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
