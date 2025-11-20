from clase_Botella import Botella

# clase Hija
class Botella_Plastica(Botella):
    def __init__(self,material,capacidad,forma,diseño,tapa,grabados,sabor):
        super().__init__(material,capacidad,forma,diseño,tapa,grabados)
        self.sabor=sabor
    
    def compatibilidad_con_bebidas(self):
        print("la bebida no es compatible con otras bebidas")
        
    def reutilizacion(self):
        print("la botella si se puede reciclar")
        
    def transparencia(self):
        print("la botella es transparente")        
        
    def imprimir_informacion(self):
        print(f"el sabor de la bebida es: {self.sabor}")
        