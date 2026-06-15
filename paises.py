# Trabajo Pratico Integrador (TPI)
# Gestion de Datos de Paises en Python


def cargar_datos():
    pass


#! Guardar datos - CSV 

def guardar_datos(nombre_archivo, paises):
    try:
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            linea = (
                pais["nombre"] + "," +
                str(pais["poblacion"]) + "," +
                str(pais["superficie"]) + "," +
                pais["continente"] + "\n"
            )

            archivo.write(linea)
        archivo.close()
    except:
        print("Error al guardar archivo")



#! Cargar datos - CSV

def cargar_datos(nombre_archivo):
    paises = []
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        archivo.readline()
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) != 4:
                continue

            pais = {
                "nombre": datos[0],
                "poblacion": int(datos[1]),
                "superficie": int(datos[2]),
                "continente": datos[3]
            }
            paises.append(pais)
        archivo.close()

    except FileNotFoundError:
        print("Error: no se encontro el archivo")
    except ValueError:
        print("Error: formato incorrecto en el CSV")

    return paises



#! Buscar PAIS

def buscar_pais(paises, nombre):
    encontrado = False
    nombre = nombre.lower().strip()
    for pais in paises:
        if nombre in pais["nombre"].lower():

            print(
                pais["nombre"],
                "| Poblacion:", pais["poblacion"],
                "| Superficie:", pais["superficie"],
                "| Continente:", pais["continente"]
            )

            encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias")



#! Agregar PAIS

def agregar_pais(paises):
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Nombre no valido")
        return
    
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("El pais ya existe")
            return
    try:
        poblacion = int(input("Poblacion: "))
        superficie = int(input("Superficie: "))
        if poblacion < 0 or superficie < 0:
            print("Los valores no pueden ser negativos")
            return
        
    except ValueError:
        print("Debe ingresar numeros")
        return

    continente = input("Continente: ").strip()
    if continente == "":
        print("Continente no valido")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_datos("paises.csv", paises)
    print("Pais agregado correctamente")



#! Actualuzar PAIS

def actualizar_pais(paises):
    nombre = input("Pais a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            
            try:
                poblacion = int(input("Nueva poblacion: "))
                superficie = int(input("Nueva superficie: "))
                if poblacion < 0 or superficie < 0:
                    print("Los valores no pueden ser negativos")
                    return

                pais["poblacion"] = poblacion
                pais["superficie"] = superficie
                guardar_datos("paises.csv", paises)
                print("Datos actualizados")

            except ValueError:
                print("Debe ingresar numeros")

            return
    print("Pais no encontrado")





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