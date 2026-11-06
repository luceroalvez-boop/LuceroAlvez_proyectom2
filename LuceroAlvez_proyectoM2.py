"""
Modulo: Proyecto M2 - Integracion de retos
Descripcion: Script que une los retos anterioresutilizando menus,
validaciones, manejo de excepciones y cumplimientode PEP 8.
"""
def mostrar_menu():
    print("\n========================")
    print("   MENU PRINCIPAL - M2    ")
    print("====================")
    print("1. Ejecutar Reto 1 (Condicionales)")
    print("2. Ejecutar Reto 2(Validaciones / Bucles)")
    print("3. Salir")
    
def ejecutar_reto_1():
    print("\n--- Ejecutando Reto 1 ---")
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad >= 18:
            print("Eres mayor de edad. ")
        else:
            print("Eres menor de edad. ")
    except ValueError:
        print("Error: Debes ingresar un numero entero valido. ")
        
def ejecutar_reto_2():
    print("\n--- Ejecutando Reto 2 ---")
    continuar = True
    while continuar:
        try:
            numero = float(input("Ingresa un nemero positivo: "))
            if numero > 0:
                print(f"¡Correcto! Ingresaste el nuemro: {numero}") 
                continuar = False
            else:
                print("El numero debe ser mayora cero. Intenta de nuevo.")
        except ValueError:
            print("Error: Entrada no valida. Por favor, introduce un numero.")
            
def main():
    bandera = True
    while bandera:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opcion (1-3): "))
            if opcion == 1:
                ejecutar_reto_1()
            elif opcion == 2:
                ejecutar_reto_2()
            elif opcion == 3:
                print("Saliendo del programa. ¡Hata luego!")
                bandera  =False
            else:
                print("Opcion invalida. Por favor seleccionea entre 1 y 3.")
        except ValueError:
            print("Error: Por favor, ingresa un numero entero valido para seleccionar una opcion.")
            
if __name__ == "__main__":
    main()