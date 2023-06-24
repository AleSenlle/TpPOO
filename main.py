from gestionar_obras import *
from modelo_orm import *

sqlite_db = GestionarObra().conectar_db()
print("Bienvenido al sistema de gestion de obras")
print("--------------------------------------------")
lista=["crear estructura de obra","cargar datos","crear 2 obras","obtener indicadores"]
i=1
for opcion in lista:
    print(str(i)+") "+opcion)
    i=i+1
print("--------------------------------------------")
opcion_elegida = int(input("Elija el número de opción: "))

while True:
    if opcion_elegida > 0 and len(lista) :
        try:
            seleccion = lista[opcion_elegida-1]
            break
        except:
            print("Ingrese una opcion correcta")
            break
    else:
        print("Ingrese un número entre 1 y "+str(len(lista)))
        opcion_elegida = int(input("Elija el número de opción: "))

if seleccion == "crear estructura de obra":
    lista = [Ebarrios, Eareas_responsables, Ecomunas, Eempresa,
             Eetapas, Obra, Etipo_obra, Etipo_contratacion, EFinanciamiento]
    GestionarObra().mapear_orm(sqlite_db, lista)
    print("Estructura creada con éxito")

if seleccion == "cargar datos":
    GestionarObra().cargar_datos(Ecomunas, Eareas_responsables, Eetapas, EFinanciamiento, Etipo_contratacion, Etipo_obra, Eempresa, Ebarrios, Obra)

if seleccion == "crear 2 obras":
    print("Ingrese los datos de obra 1")
    obra1 = GestionarObra().nueva_obra(Obra, Etipo_obra, Eareas_responsables, Ebarrios, Eetapas)
    print("Ingrese los datos de obra 2")
    obra2 = GestionarObra().nueva_obra(Obra, Etipo_obra, Eareas_responsables, Ebarrios, Eetapas)
    print("Obras creadas con exito")
    print("¿Desea pasar por los diferentes estados de la obra?")
    lista=["si","no"]
    i=1
    for opcion in lista:
        print(str(i)+") "+opcion)
        i=i+1
    respuesta = int(input("Elija el número de opción: "))
    opcion_elegida = lista[respuesta-1]
    if opcion_elegida == "si":
        print("Ingrese los datos de proyecto 1")
        obra1.nuevo_proyecto()
        print("--------------------------------------------")
        print("Ingrese los datos de proyecto 2")
        print("--------------------------------------------")
        obra2.nuevo_proyecto()
        print("Proyectos creados con exito")
        print("--------------------------------------------")
        obra1.save()
        obra2.save()
        print("Ingrese la contratación de la obra 1: ")
        print("--------------------------------------------")
        obra1.iniciar_contratacion()
        print("Ingrese la contratación de la obra 2:")
        print("--------------------------------------------")
        obra2.iniciar_contratacion()
        obra1.save()
        obra2.save()
        print("Ingrese la adjudicación de la obra 1: ")
        print("--------------------------------------------")
        obra1.adjudicar_obra()
        print("Ingrese la adjudicación de la obra 2: ")
        print("--------------------------------------------")
        obra2.adjudicar_obra()
        print("Ingrese la adjudicación de la obra 2: ")
        print("--------------------------------------------")
        obra1.save()
        obra2.save()
        print("Ingrese el inicio de la obra 1: ")
        print("--------------------------------------------")
        obra1.iniciar_obra()
        print("Ingrese el inicio de la obra 2: ")
        print("--------------------------------------------")
        obra2.iniciar_obra()
        obra1.save()
        obra2.save()
        print("--------------------------------------------")
        print("Ingrese el avance de la obra 1: ")
        print("--------------------------------------------")
        obra1.actualizar_porcentaje_avance()
        print("Ingrese el avance de la obra 2: ")
        print("--------------------------------------------")
        obra2.actualizar_porcentaje_avance()
        obra1.save()
        obra2.save()
        print("--------------------------------------------")
        print("Ingrese el plazo incrementado de la obra 1: ")
        print("--------------------------------------------")
        obra1.incrementar_plazo()
        print("Ingrese el plazo incrementado de la obra 2: ")
        print("--------------------------------------------")
        obra2.incrementar_plazo()
        obra1.save()
        obra2.save()
        print("--------------------------------------------")
        print("Ingrese la cantidad de empleados que desea agregar a la obra 1: ")
        print("--------------------------------------------")
        obra1.incrementar_mano_obra()
        obra1.save()
        print("Se desea rescindir la obra 2")
        print("--------------------------------------------")
        obra2.rescindir_obra()
        print("Se finalizará la obra 1")
        print("--------------------------------------------")
        obra1.finalizar_obra()
        obra1.save()
        obra2.save()

if seleccion == "obtener indicadores":
    GestionarObra().obtener_indicadores(Obra, Etipo_obra,
                                        Eareas_responsables, Ebarrios, Eetapas)
