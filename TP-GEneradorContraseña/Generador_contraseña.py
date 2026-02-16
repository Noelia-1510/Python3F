import secrets, string, sys


diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

def generar_contraseña(longitud, opciones):
    contraseña = ''.join(secrets.choice(opciones) for i in range(longitud))
    return contraseña

def menu():
    while True:
        print("∎▪---------------ωєℓƈօʍɛ---------------▪∎\n")
        print("   ", "Generador de Contraseñas V0.1")
        print("\n•»--------------(• ∘ •)-----------------«•\n")
        print("Seleccione una de las siguientes opciones: \n")
        print("» 1. Generar contraseña solo de Letras.")
        print("» 2. Generar contraseña solo de Numeros.")
        print("» 3. Generar contraseña Letras y Numeros.")
        print("» 4. Generar contraseña Letras, Numeros y Caracteres.")
        print("» 0. Salir.")
        opcion = input("\nEscriba la opcion seleccionada: ")

        if opcion == "1":
            opciones = diccionario['letras']
        elif opcion == "2":
            opciones = diccionario['numeros']
        elif opcion == "3":
            opciones = diccionario['letras'] + diccionario['numeros']
        elif opcion == "4":
            opciones = diccionario['letras'] + diccionario['numeros'] + diccionario["caracteres"]
        elif opcion == "0":
            print("Cerrando programa...")
            break

        longitud = int(input("\nIngrese la longitud que quiere que tenga la contraseña: "))
        contraseña = generar_contraseña(longitud, opciones)
        print("\n•»---------------------------------«•")
        print("   ",f"Su contraseña es: {contraseña}")
        print("•»---------------------------------«•")

        salir = input("\n¿Desea salir? (s/n): \n")
        if salir.lower() == 's':
            print("Cerrando programa...")
            break

if __name__ == "__main__":
    menu()



