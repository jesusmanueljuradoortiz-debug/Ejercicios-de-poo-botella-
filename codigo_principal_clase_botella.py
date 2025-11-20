from clase_hija_botella import Botella_Plastica

# ***** Codigo Principal *****
# se crea la instancia del objeto
Envase1 = Botella_Plastica("plastico","330 ml","robusta","largo","plastico","texto de la etiqueta","manzana")
Envase2 = Botella_Plastica("vidrio","330 ml","robusta","largo","metalica","texto de la etiqueta","manzana")
# se llama el metodo del objeto
Envase1.imprimir_informacion()
Envase1.contener_liquidos()
Envase1.facilitar_el_vertido()
Envase1.cierre_hermetico()
Envase1.transporte()
Envase1.manejo()
Envase1.compatibilidad_con_bebidas()
Envase1.reutilizacion()
Envase1.transparencia()
print("zona envase2")
Envase2.imprimir_informacion()
Envase2.contener_liquidos()
Envase2.facilitar_el_vertido()
Envase2.cierre_hermetico()
Envase2.transporte()
Envase2.manejo()
Envase2.compatibilidad_con_bebidas()
Envase2.reutilizacion()
Envase2.transparencia()
