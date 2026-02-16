import pickle, sys, os, random


def limpiar_pantalla():
    if os.name == 'nt': 
        os.system('cls')

def generar_numero_ticket():
    return random.randrange(1000, 9999)

def guardar_ticket(nombre_archivo, ticket):
    with open(nombre_archivo, "wb") as f:
        pickle.dump(ticket, f)

def cargar_ticket(nombre_archivo):
    with open(nombre_archivo, "rb") as f:
        return pickle.load(f)

def existe_ticket(nombre_archivo):
    return os.path.isfile(nombre_archivo)

def menu_principal():
    limpiar_pantalla()
    print("  ","Hola bienvenido al sistema de Tickets\n")
    print("1 - Generar un Nuevo Ticket")
    print("2 - Leer un Ticket")
    print("3 - Salir")
    opcion = input("Seleccione: ")
    return opcion

def crear_ticket():
    print("\nIngrese los datos para Generar un nuevo Ticket")
    nombre = input("Ingrese su Nombre: ")
    sector = input("Ingrese su Sector: ")
    asunto = input("Ingrese Asunto: ")
    mensaje = input("Ingrese un Mensaje: ")

    numero_ticket = generar_numero_ticket()
    ticket = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'mensaje': mensaje,
        'numero_ticket': numero_ticket
    }

    nombre_archivo = f"ticket_{numero_ticket}.pkl"
    guardar_ticket(nombre_archivo, ticket)

    limpiar_pantalla()
    print("=================================================")
    print("       ","Se genero el siguiente Ticket")
    print("=================================================")
    print(f"Su nombre: {nombre}    N°Ticket: {numero_ticket}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"\nMensaje: {mensaje}\n")
    print("Recordar su numero de Ticket\n")
    
    if input("¿Desea generar un nuevo Ticket? (s/n): ").lower() == 's':
        crear_ticket()

def leer_ticket():
    limpiar_pantalla()
    numero_ticket = input("Ingrese el numero de Ticket: ")
    nombre_archivo = f"ticket_{numero_ticket}.pkl"
    
    if existe_ticket(nombre_archivo):
        ticket = cargar_ticket(nombre_archivo)
        print("\nTicket almacenado:")
        print("=======================================")
        print(f"Su nombre: {ticket['nombre']}    N°Ticket: {ticket['numero_ticket']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"\nMensaje: {ticket['mensaje']}\n")
    else:
        print("\nTicket no encontrado.")
    
    if input("¿Desea leer otro Ticket? (s/n): ").lower() == 's':
        leer_ticket()

def main():
    while True:
        opcion = menu_principal()
        if opcion == '1':
            crear_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if input("\n¿Está seguro que desea salir? (s/n): ").lower() == 's':
                sys.exit()
        else:
            print("Opción no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()
