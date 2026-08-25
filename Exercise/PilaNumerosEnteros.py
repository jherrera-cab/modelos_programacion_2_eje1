def PilaNumInt():
    # Funciones para la Lista Enlazada
    def crear_nodo(valor):
        return {"valor": valor, "siguiente": None}

    def insertar_pila(cabeza, valor):
        nuevo = crear_nodo(valor)
        nuevo["siguiente"] = cabeza
        return nuevo  # Retorna la nueva cabeza

    def obtener_elementos(cabeza):
        elementos = []
        actual = cabeza
        while actual is not None:
            elementos.append(actual["valor"])
            actual = actual["siguiente"]
        return elementos

    def procesar_datos(cabeza):
        elementos = obtener_elementos(cabeza)
        if not elementos:
            return

        pares = sum(1 for x in elementos if x % 2 == 0)
        promedio = sum(elementos) / len(elementos)
        ultimo_dato = elementos[0]  # El último ingresado quedó al tope de la pila

        print("Los datos de la lista son:")
        print(", ".join(map(str, elementos)))
        print("La cantidad de números pares")
        print(pares)
        print("El promedio es")
        print(f"{promedio:.2f}".replace('.', ','))
        print("El último dato de la lista es:")
        print(ultimo_dato)

    # Programa principal
    lista = None
    n = int(input("¿Cuántos elementos desea ingresar?: "))

    for i in range(n):
        val = int(input(f"Ingrese el dato {i + 1}: "))
        lista = insertar_pila(lista, val)

    print("\n--- SALIDA ---")
    procesar_datos(lista)