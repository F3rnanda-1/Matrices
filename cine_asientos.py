def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]


def mostrar_sala(sala):
    print("\nEstado actual de la sala:\n")
    for fila in sala:
        print(" ".join(fila))
    print()


def reservar_asiento(sala, fila, columna):
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("El asiento no existe.")
        return
    if sala[fila][columna] == 'X':
        print("El asiento ya está ocupado.")
    else:
        sala[fila][columna] = 'X'
        print("Asiento reservado.")


def liberar_asiento(sala, fila, columna):
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("El asiento no existe.")
        return
    if sala[fila][columna] == 'L':
        print("El asiento está libre.")
    else:
        sala[fila][columna] = 'L'
        print("Asiento liberado.")


def contar_asientos(sala):
    libres = sum(fila.count('L') for fila in sala)
    ocupados = sum(fila.count('X') for fila in sala)
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")


def main():
    print("SISTEMA DE ASIENTOS DEL CINE")
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))

    sala = crear_sala(filas, columnas)

    while True:
        print("\nMenú:")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_sala(sala)
        elif opcion == '2':
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
            reservar_asiento(sala, f, c)
        elif opcion == '3':
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
            liberar_asiento(sala, f, c)
        elif opcion == '4':
            contar_asientos(sala)
        elif opcion == '5':
            print("Hasta luego")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
