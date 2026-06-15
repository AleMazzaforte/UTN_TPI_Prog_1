# Trabajo Pratico Integrador (TPI)
# Gestion de Datos de Paises en Python


def cargar_datos():
    pass


#º  MENU

def mostrar_menu():
    print("\n========= MENU =========")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar continente")
    print("5. Filtrar poblacion")
    print("6. Filtrar superficie")
    print("7. Ordenar por nombre")
    print("8. Ordenar por poblacion")
    print("9. Ordenar por superficie")
    print("10. Estadisticas")
    print("11. Salir")
    print()


#ç MAIN

def main():
    paises = cargar_datos()
    opcion = 0

    while opcion != 11:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                pass

            elif opcion == 2:
                pass

            elif opcion == 3:
                pass

            elif opcion == 4:
                pass

            elif opcion == 5:
                pass

            elif opcion == 6:
                pass

            elif opcion == 7:
                pass

            elif opcion == 8:
                pass

            elif opcion == 9:
                pass

            elif opcion == 10:
                pass

            elif opcion == 11:
                print("Programa finalizado")

            else:
                print("Opcion no valida")

        except ValueError:
            print("Debe ingresar un numero")

main()