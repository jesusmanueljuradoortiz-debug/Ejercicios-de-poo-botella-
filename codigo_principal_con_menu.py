from clase_hija_botella import Botella_Plastica
from base_datos_clase_botella import base_datos_botella

data = base_datos_botella()

def crear_botella():
    print("\n crear una botella")
    material = input("Material: ")
    capacidad = input("Capacidad: ")
    forma = input("Forma: ")
    diseño = input("Diseño: ")
    tapa = input("¿Tiene tapa? (s/n): ").lower() == "s"
    grabados = input("Grabados: ")
    sabor = input("sabor: ")

    nuevo = Botella_Plastica(material,capacidad,forma,diseño,tapa,grabados,sabor)
    data.guardar_botella(nuevo)

def mostrar_info_guardada():
    data.mostrar_informacion()

def eliminar_botella():
    mostrar_info_guardada()
    try:
        indice = int(input("\n ingresa el numero de la botella a eliminar"))
        data.eliminar_botella(indice)
    except ValueError:
        print("numero no valido. \n")

def mostrar_detalle_contenido():
    mostrar_info_guardada()
    try:
        indice = int(input("\ningresa numero de botella para ver el contenido"))
        if 0 <= indice < len(data.lista_botellas):
            Botella = data.lista_botellas[indice]
            print("\n contenido de la botella ")
            Botella.imprimir_informacion()
            Botella.contener_liquidos()
            Botella.facilitar_el_vertido()
            Botella.cierre_hermetico()
            Botella.transporte()
            Botella.manejo()
            Botella.compatibilidad_con_bebidas()
            Botella.reutilizacion()
            Botella.transparencia()
        else:
            print("\n el numero no esta en base de datos.")
    except ValueError:
        print("numero no valido \n")

def fin_programa():
    print("fin del programa")

while True:
    print("menu")
    print("1) crear botella")
    print("2) mostrar la botella creada")
    print("3) ver contenido")
    print("4) eliminar botella")
    print("5) salir")

    opcion = input("selecione una opcion")

    if opcion == "1":
        crear_botella()
    elif opcion == "2":
        mostrar_info_guardada()
    elif opcion == "3":
        mostrar_detalle_contenido()
    elif opcion == "4":
        eliminar_botella()
    elif opcion == "5":
        fin_programa()
        break
    else:
        print("no valida esta opcion")