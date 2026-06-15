# Trabajo Pratico Integrador (TPI)
# Gestion de Datos de Paises en Python

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
                "nombre": datos[0].lower(),
                "poblacion": int(datos[1]),
                "superficie": int(datos[2]),
                "continente": datos[3].lower()
            }
            paises.append(pais)
        archivo.close()
        
    except FileNotFoundError:
        print("Error: no se encontro el archivo")
    except ValueError:
        print("Error: formato incorrecto en el CSV")

    return paises



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
    minimo, maximo = pedir_rango("población")
    resultado = filtrar_por_rango(paises, "poblacion", minimo, maximo)
    mostrar_resultado_filtro(resultado)


def filtrar_superficie(paises):
    print("Filtro por superficie en Km²")
    minimo, maximo = pedir_rango("superficie")
    resultado = filtrar_por_rango(paises, "superficie", minimo, maximo)
    mostrar_resultado_filtro(resultado)



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
                pass

            elif opcion == 2:
                pass

            elif opcion == 3:
                pass

            elif opcion == 4:
                filtrar_continente(paises)

            elif opcion == 5:
                filtrar_poblacion(paises)

            elif opcion == 6:
                filtrar_superficie(paises)

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