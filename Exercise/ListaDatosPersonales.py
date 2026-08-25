
def listDataPersonal():
    # Funciones para la Lista Enlazada de Personas
    def crear_nodo_persona(codigo, nombre, telefono, edad):
        persona = {
            "codigo": codigo,
            "nombre": nombre,
            "telefono": telefono,
            "edad": edad
        }
        return {"persona": persona, "siguiente": None}

    def insertar_pila(cabeza, codigo, nombre, telefono, edad):
        nuevo = crear_nodo_persona(codigo, nombre, telefono, edad)
        nuevo["siguiente"] = cabeza
        return nuevo  # Retorna la nueva cabeza

    def eliminar_primero(cabeza):
        if cabeza is not None:
            return cabeza["siguiente"]  # Avanza al siguiente nodo
        return None

    def mostrar_lista(cabeza):
        elementos = []
        actual = cabeza
        while actual is not None:
            p = actual["persona"]
            texto = f"({p['codigo']}, {p['nombre']}, {p['telefono']}, {p['edad']})"
            elementos.append(texto)
            actual = actual["siguiente"]
        print(", ".join(elementos))

    def contar_elementos(cabeza):
        contador = 0
        actual = cabeza
        while actual is not None:
            contador += 1
            actual = actual["siguiente"]
        return contador

    # Programa principal
    lista_personas = None
    n = int(input("¿Cuántas personas ingresará?: "))

    for i in range(n):
        print(f"\nPersona {i + 1}")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        edad = input("Edad: ")
        lista_personas = insertar_pila(lista_personas, codigo, nombre, telefono, edad)

    print("\nLos elementos de la lista son:")
    mostrar_lista(lista_personas)

    print("\nRetirar un elemento de la lista y mostrar nuevos elementos de la lista:")
    lista_personas = eliminar_primero(lista_personas)
    mostrar_lista(lista_personas)

    print("\nContar los elementos de la lista:")
    print(contar_elementos(lista_personas))