class base_datos_botella:
    def __init__(self):
        self.lista_botellas = []

    def guardar_botella(self, nueva_botella):
        self.lista_botellas.append(nueva_botella)
        print(" se a creado con exito la botella. \n")

    def mostrar_informacion(self):
        if not self.lista_botellas:
            print("no hay botellas guardadas")
            return
        
        for i,botella in enumerate(self.lista_botellas):
            print(f"\n botella N° {i}")
            botella.imprimir_informacion()

    def eliminar_botella(self,indice):
        if 0 <= indice < len(self.lista_botellas):
            self.lista_botellas.pop(indice)
            print("la botella a sido eliminada correctamente")
        else:
            print("no existe este numero")

        