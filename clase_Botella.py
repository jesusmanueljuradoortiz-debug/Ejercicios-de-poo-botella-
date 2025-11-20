# se crea la clase
class Botella:
    # se crea el metodo constructor
    def __init__(self,material,capacidad,forma,diseño,tapa,grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados
        
        
    def contener_liquidos(self):
        print(f"la botella de {self.material} contiene liquido")
        
    def facilitar_el_vertido(self):
        print(f"la botella facilita el vertido")
        
    def cierre_hermetico(self):
        print(f"la botella tiene cierre hermetico")
        
    def transporte(self):
        print(f"la botella tiene el transporte")
        
    def manejo(self):
        print(f"la botella tiene manejo")
        
    def imprimir_informacion(self):
        print(f"capacidad {self.capacidad} ")
        print(f"forma {self.forma}")
        print(f"diseño {self.diseño}")
        print(f"tapa {self.tapa}")
        print(f"grabados {self.grabados}")
        
