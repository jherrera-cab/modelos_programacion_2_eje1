from Exercise.ListaDatosPersonales import listDataPersonal
from Exercise.PilaNumerosEnteros import PilaNumInt

if __name__ == '__main__':
    while True:
        print("\n---------------------------")
        print("    MENÚ DE OPCIONES")
        print("---------------------------")
        print("1. Lista datos personales")
        print("2. Pila números enteros")
        print("3. Salir")
        print("---------------------------")
        
        try:
            option = int(input("Que función desea ejecutar: "))
        except ValueError:
            print("\nError: Debe ingresar un número entero válido.")
            continue

        if option == 1:
            listDataPersonal()
        elif option == 2:
            PilaNumInt()
        elif option == 3:
            print("\nSaliendo de la ejecución...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")