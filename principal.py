from paquete_academico.modelo import *

c = Ciudad()
c.agregar_nombre_ciudad("Loja")
c.agregar_poblacion(200000)


est1 = EstPresencial()
est1.agregar_ciudad(c)
est1.agregar_ID_estudiante(12334)
est1.agregar_nombre("David")
est1.agregar_apellido("Diaz")
est1.agregar_ciclo(8)
est1.agregar_numero_creditos(189)

print(est1.presentar_datos())
