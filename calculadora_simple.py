# Función para sumar
def sumar(x, y):
    return x + y

# Función para restar
def restar(x, y):
    return x - y

# Función para mostrar el menú
def mostrar_menu():
    print("\nOperaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

# Función principal de la calculadora
def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1/2/3): ")

        # Si el usuario elige salir
        if opcion == '3':
            print("¡Hasta luego!")
            break

        # Asegurarse de que la opción es válida
        if opcion not in ['1', '2']:
            print("Opción no válida. Intenta de nuevo.")
            continue

        # Pedir los números para la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        # Realizar la operación seleccionada
        if opcion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")

# Ejecutar la calculadora
calculadora()
