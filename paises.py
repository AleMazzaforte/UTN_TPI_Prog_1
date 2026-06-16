# Trabajo Pratico Integrador (TPI)
# Gestion de Datos de Paises en Python

def cargar_datos(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.readline()
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) != 4:
                    continue

                pais = {
                    "nombre": datos[0].lower(),
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3].lower()
                }
                paises.append(pais)
            
        
    except FileNotFoundError:
        print("Error: no se encontro el archivo")
    except ValueError:
        print("Error: formato incorrecto en el CSV")

    return paises

def pausar():
    input("Presione Enter para continuar...")

#################################
###     FILTRAR 
#################################
def filtrar_continente(paises):
    try:
        entrada = input("Ingrese busqueda ").lower().strip()
        if not entrada:
            raise ValueError("No ingresó ningún valor. Intente nuevamente.")

        encontrado = []
        for pais in paises:
            if pais["continente"] == entrada:
                encontrado.append(pais["nombre"])
        
        if encontrado:
            for pais in encontrado:
                print(pais.title())
        else:
            print("No se encontraron paises para ese continente.")
        
    except ValueError as e:
        print(f"Error: {e}")

#FILTRAR POR RANGO NUMERICO para filtrar por superficie y poblacion
def filtrar_por_rango(paises, campo, minimo, maximo):
    resultado = []

    for pais in paises:
        if minimo <= pais[campo] <= maximo:
            resultado.append(pais)

    return resultado

def pedir_rango():
    while True:
        try:
            minimo = int(input("Mínimo: ").strip())
            maximo = int(input("Máximo: ").strip())

            if minimo <= 0 or maximo <= 0:
                raise ValueError("Los valores deben ser números positivos.")

            if maximo <= minimo:
                raise ValueError("El máximo debe ser mayor que el mínimo.")

            return minimo, maximo

        except ValueError as e:
            print(f"Error: {e}")

def mostrar_resultado_filtro(resultado):

    if not resultado:
        print("No se encontraron resultados.")
        return
    
    for pais in resultado:
        print(f"Nombre: {pais['nombre'].title()}. Poblacion: {pais['poblacion']}. Superficie: {pais['superficie']}. Continente: {pais['continente'].title()}.")

def filtrar_poblacion(paises):
    print("Filtro por población")
    minimo, maximo = pedir_rango()
    resultado = filtrar_por_rango(paises, "poblacion", minimo, maximo)
    mostrar_resultado_filtro(resultado)

def filtrar_superficie(paises):
    print("Filtro por superficie en Km²")
    minimo, maximo = pedir_rango()
    resultado = filtrar_por_rango(paises, "superficie", minimo, maximo)
    mostrar_resultado_filtro(resultado)


#################################
###     ORDENAR 
#################################

# Pedir ordenamiento ascendente o descendente
def opcion_ordenar():

    while True:

        try:

            opcion = input(
                "1-Ascendente 2-Descendente: "
            ).strip()

            if opcion not in ["1", "2"]:
                raise ValueError(
                    "Debe ingresar 1 o 2."
                )

            return opcion

        except ValueError as e:
            print(f"Error: {e}")

# Funcion para ordenar
def ordenar_paises(paises, campo):

    try:

        if not paises:
            raise ValueError(
                "No hay países cargados."
            )

        opcion = opcion_ordenar()

        cantidad = len(paises)

        for _ in range(cantidad):

            for j in range(cantidad - 1):

                if opcion == "1":

                    if paises[j][campo] > paises[j + 1][campo]:

                        aux = paises[j]
                        paises[j] = paises[j + 1]
                        paises[j + 1] = aux

                else:

                    if paises[j][campo] < paises[j + 1][campo]:

                        aux = paises[j]
                        paises[j] = paises[j + 1]
                        paises[j + 1] = aux

        print("Ordenamiento completado")

        return paises

    except KeyError:
        print(
            f"El campo '{campo}' no existe."
        )

    except ValueError as e:
        print(f"Error: {e}")


def ordenar_nombre(paises):

    ordenar_paises(paises, "nombre")

    for pais in paises[:10]:

        print(pais["nombre"].title())


def ordenar_poblacion(paises):

    ordenar_paises(paises, "poblacion")

    for pais in paises[:10]:

        print(
            f"{pais['nombre'].title()} - "
            f"{pais['poblacion']}"
        )


def ordenar_superficie(paises):

    ordenar_paises(paises, "superficie")

    for pais in paises[:10]:

        print(
            f"{pais['nombre'].title()} - "
            f"{pais['superficie']} km²"
        )

#################################################
### ESTADISTICAS
#################################################

def mostrar_estadisticas(paises):

    try:

        if not paises:
            raise ValueError(
                "No hay datos cargados."
            )

        mayor = paises[0]
        menor = paises[0]

        suma_poblacion = 0
        suma_superficie = 0

        continentes = {}

        for pais in paises:

            if pais["poblacion"] > mayor["poblacion"]:
                mayor = pais

            if pais["poblacion"] < menor["poblacion"]:
                menor = pais

            suma_poblacion += pais["poblacion"]
            suma_superficie += pais["superficie"]

            continente = pais["continente"]

            if continente in continentes:
                continentes[continente] += 1
            else:
                continentes[continente] = 1

        promedio_poblacion = (
            suma_poblacion / len(paises)
        )

        promedio_superficie = (
            suma_superficie / len(paises)
        )

        print("\n=== ESTADISTICAS ===")

        print(
            "Mayor poblacion:",
            mayor["nombre"].title(),
            "-",
            mayor["poblacion"]
        )

        print(
            "Menor poblacion:",
            menor["nombre"].title(),
            "-",
            menor["poblacion"]
        )

        print(
            "Promedio poblacion:",
            round(promedio_poblacion, 2)
        )

        print(
            "Promedio superficie:",
            round(promedio_superficie, 2)
        )

        print("\nCantidad de paises por continente:")

        for continente in continentes:

            print(
                continente.title(),
                ":",
                continentes[continente]
            )

    except ValueError as e:
        print(f"Error: {e}")

    except KeyError as e:
        print(
            f"Error: falta la clave {e} en algún país."
        )

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





#! Buscar PAIS

def buscar_pais(paises):
    encontrado = False
    nombre = input("Ingrese su búsqueda ").lower().strip()
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
    paises = cargar_datos("paises.csv")
    opcion = 0

    while opcion != 11:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                agregar_pais(paises)
                pausar()

            elif opcion == 2:
                actualizar_pais(paises)
                pausar()

            elif opcion == 3:
                buscar_pais(paises)
                pausar()

            elif opcion == 4:
                filtrar_continente(paises)
                pausar()

            elif opcion == 5:
                filtrar_poblacion(paises)
                pausar()

            elif opcion == 6:
                filtrar_superficie(paises)
                pausar()

            elif opcion == 7:
                ordenar_nombre(paises)
                pausar()

            elif opcion == 8:
                ordenar_poblacion(paises)
                pausar()

            elif opcion == 9:
                ordenar_superficie(paises)
                pausar()

            elif opcion == 10:
                mostrar_estadisticas(paises)
                pausar()

            elif opcion == 11:
                print("Programa finalizado")

            else:
                print("Opcion no valida")

        except ValueError:
            print("Debe ingresar un numero")

main()