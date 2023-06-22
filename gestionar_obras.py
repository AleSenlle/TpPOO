from peewee import *
import pandas as pd
from abc import ABCMeta
import os
import numpy as np


class GestionarObra(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    # Este es el punto 4.A
    @classmethod
    def extraer_datos(self):
        try:
            archivo_csv = os.getcwd()+"/"+"observatorio-de-obras-urbanas.csv"
            df = pd.read_csv(archivo_csv, sep=",")
            return df
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return False

    # Este es el punto 4.B
    @classmethod
    def conectar_db(self):
        sqlite_db = SqliteDatabase(
            os.getcwd()+'/'+'obras_urbanas.db', pragmas={'journal_mode': 'wal'})
        try:
            sqlite_db.connect()
            # La base de datos se crea cuando intenta conectarse por primera vez y no la encuentra.
            return sqlite_db
        except OperationalError as e:
            print("Se ha generado un error en la conexion a la BD.", e)
            exit()

    # Este es el punto 4.C
    @classmethod
    def mapear_orm(self, sqlite_db, lista):
        sqlite_db.create_tables(lista)

    # Este es el punto 4.D
    @classmethod
    def limpiar_datos(self):
        df = self.extraer_datos()
        print(df)
        print("limpiando datos")
        df.dropna(subset=["monto_contrato", "comuna", "barrio", "direccion", "etapa",
                  "tipo", "area_responsable", "descripcion", ], axis=0, inplace=True)
        print(df)
        return df

    # Este es el punto 4.E
    @classmethod
    def normalizar_etapas(self, etapa):
        mapeo = {
            'Proc. Adm': 'Proyecto',
            'Licitación': 'Proyecto',
            'Sin iniciar': 'Proyecto',
            'Rescindida': 'Rescindida',
            'En ejecución': 'Inicializada',
            'En obra': 'Inicializada',
            'Desestimada': 'Rescindida',
            'En licitación': 'Proyecto',
            'Neutralizada': 'Rescindida',
            'Pausada': 'Inicializada',
            'Inicial': 'Inicializada',
            'En Ejecución': 'Inicializada',
            'Adjudicada': 'Proyecto',
            'Finalizada': 'Finalizada',
        }
        return mapeo.get(etapa, 'Proyecto')

    @classmethod
    def cargar_datos(self, Ecomunas, Eareas_responsables, Eetapas, EFinanciamiento, Etipo_contratacion, Etipo_obra, Eempresa, Ebarrios, Obra):
        df = self.limpiar_datos()

        data_unique = list(df['comuna'].unique())
        print(data_unique)
        for elem in data_unique:
            print("Elemento:", elem)
            try:
                Ecomunas.create(nro_comuna=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Comuna.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        data_unique = list(df['area_responsable'].unique())
        print(data_unique)
        for elem in data_unique:
            print("Elemento:", elem)
            try:
                Eareas_responsables.create(descripcion=elem)
            except IntegrityError as e:
                print(
                    "Error al insertar un nuevo registro en la tabla Area Responsable.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        df['etapa'] = df['etapa'].apply(self.normalizar_etapas)
        data_unique = list(df['etapa'].unique())
        print(data_unique)
        for elem in data_unique:
            print("Elemento:", elem)
            try:
                Eetapas.create(descripcion=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Etapa.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        data_unique = list(df['financiamiento'].unique())
        print(data_unique)
        for elem in data_unique:
            if elem is not np.nan:
                print("Elemento:", elem)
                try:
                    EFinanciamiento.create(descripcion=elem)
                except IntegrityError as e:
                    print(
                        "Error al insertar un nuevo registro en la tabla Financiamiento.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        data_unique = list(df['contratacion_tipo'].unique())
        print(data_unique)
        for elem in data_unique:
            if elem is not np.nan:
                print("Elemento:", elem)
                try:
                    Etipo_contratacion.create(descripcion=elem)
                except IntegrityError as e:
                    print(
                        "Error al insertar un nuevo registro en la tabla Tipo de Contratacion.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        data_unique = list(df['tipo'].unique())
        print(data_unique)
        for elem in data_unique:
            print("Elemento:", elem)
            try:
                Etipo_obra.create(descripcion=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Tipo de Obra.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        # Ahora normalizo las tablas que tienen +2 columnas:
        df.drop_duplicates(subset=['nombre'], inplace=True)
        for elem in df.values:
            if elem is not np.nan:
                try:

                    Obra.create(entorno=elem[1], nombre=elem[2], descripcion=elem[6], monto_contrato=elem[7], direccion=elem[10], fecha_inicio=elem[13], fecha_fin_inicial=elem[14], plazo_meses=elem[15], porcentaje_avance=0.0, licitacion_anio=elem[22],
                                nro_contratacion=elem[24], beneficiarios=elem[26], mano_obra=elem[27], expediente_numero=elem[33], etapa=elem[3], empresa=elem[21], tipo_obra=elem[4], area_responsable=elem[5], barrio=elem[9], tipo_contratacion=elem[23])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla obras.", e)
        print("Se han persistido las obras en la BD.")

        df.drop_duplicates(subset=['licitacion_oferta_empresa'], inplace=True)
        for elem in df.values:
            if elem is not np.nan:
                print(elem)
                try:
                    Eempresa.create(cuit=elem[25], razonSocial=elem[21])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla Empresa.", e)
        print("Se han persistido los tipos de Empresas en la BD.")

        df.drop_duplicates(subset=['barrio'], inplace=True)
        for elem in df.values:
            if elem is not np.nan:
                print(elem)
                try:
                    Ebarrios.create(nombre=elem[9], nro_comuna=elem[8])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla barrio.", e)
        print("Se han persistido los barrios en la BD.")

 # este es el punto 4.F
    @classmethod
    def nueva_obra(self, Obra, Etipo_obra, Eareas_responsables, Ebarrios, Eetapas):
        sqlite_db = self.conectar_db()

        print("Conexión exitosa a la base de datos")
        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Etipo_obra.select().where(Etipo_obra.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("los tipos de obras son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 25:
                try:
                    tipo_obra = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 24")
                opcion_elegida = int(input("Elija el número de opción: "))

        entorno = input("Ingrese el entorno: ")
        nombre = input("Ingrese el nombre: ")

        sqlite_db = self.conectar_db()
        print("Conexión exitosa a la base de datos")

        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Eareas_responsables.select().where(
            Eareas_responsables.descripcion != ' ')
        resultados = list(query)
        

        # Recorre los resultados y muestra la descripción
        print("las areas responsables son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 21:
                try:
                    area_responsable = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 20")
                opcion_elegida = int(input("Elija el número de opción: "))

        descripcion = input("Ingrese una descripción: ")
        monto_contrato = input("Ingrese el monto del contrato: ")

        sqlite_db = self.conectar_db()
        print("Conexión exitosa a la base de datos")

        # Consulta a la base de datos
        query = Ebarrios.select().where(Ebarrios.nombre != ' ')
        resultados = list(query)
        print("los barrios son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.nombre)
            i = i+1
            lista.append(resultado.nombre)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 57:
                try:
                    barrio = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 56")
                opcion_elegida = int(input("Elija el número de opción: "))

        direccion = input("Ingrese la dirección: ")
        plazo_meses = input("Ingrese el plazo de meses: ")
        beneficiarios = input("Ingrese quienes son los beneficiarios: ")

        query = Eetapas.select().where(Eetapas.descripcion != ' ')
        resultados = list(query)
        print("las etapas son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 5:
                try:
                    etap = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 4")
                opcion_elegida = int(input("Elija el número de opción: "))

        empre = input("Ingrese la empresa: ")
        tipo_contrat = "sin asignar"

        obra = Obra(entorno=entorno, nombre=nombre, tipo_obra=tipo_obra, area_responsable=area_responsable,
                    descripcion=descripcion, monto_contrato=monto_contrato, barrio=barrio, direccion=direccion,
                    plazo_meses=plazo_meses, beneficiarios=beneficiarios, etapa=etap, empresa=empre, tipo_contratacion=tipo_contrat)

        obra.save()
        return obra

    # este es el punto 4.G
    @classmethod
    def obtener_indicadores(self, Obra,Etipo_obra, Eareas_responsables, Ebarrios, Eetapas):
        # a. Listado de todas las áreas responsables.
        sqlite_db = self.conectar_db()
        print("Conexión exitosa a la base de datos")

        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Eareas_responsables.select().where(
            Eareas_responsables.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("las areas responsables son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")
        # b. Listado de todos los tipos de obra.
        sqlite_db = self.conectar_db()
        print("Conexión exitosa a la base de datos")

        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Etipo_obra.select().where(Etipo_obra.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("los tipo de obra son :")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")
        
        # c. Cantidad de obras que se encuentran en cada etapa.
        sqlite_db = self.conectar_db()
        print("Conexión exitosa a la base de datos")

        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Finalizada')
        query2 = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Inicializada')
        query3 = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Rescindida')
        query4 = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Proyecto')
        count = query.scalar()
        count2 = query2.scalar()
        count3 = query3.scalar()
        count4 = query4.scalar()
        print("la cantidad de obras finalizadas son: "+str(count))
        print("la cantidad de obras inicializadas son: "+str(count2))
        print("la cantidad de obras rescindidas son: "+str(count3))
        print("la cantidad de obras en proyecto son: "+str(count4))
        print("-----------------------------------------------")
        
        # d.  Cantidad de obras por tipo de obra.
        query = Etipo_obra.select().where(Etipo_obra.descripcion != ' ')
        resultados = list(query)
        for resultado in resultados:
            query = Obra.select(fn.COUNT()).where(Obra.tipo_obra_id == resultado.descripcion)
            count = query.scalar()
            print("la cantidad de obras de tipo "+str(resultado.descripcion)+" son: "+str(count))
        print("-----------------------------------------------")
        
        #e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
        query = Ebarrios.select().where(Ebarrios.nro_comuna_id ==
                                        '1' or Ebarrios.nro_comuna_id == '2' or Ebarrios.nro_comuna_id == '3')
        resultados = list(query)
        for resultado in resultados:
            print("los barrios de las comunas 1, 2 y 3 son: "+str(resultado.nombre))
        print("-----------------------------------------------")
        
        # f. Cantidad de obras “Finalizadas” en la comuna 1.
        suma=0
        for resultado in resultados:
            query = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Finalizada' and Obra.barrio_id == resultado.nombre)
            count = query.scalar()
            suma=suma+count
        print("la cantidad de obras finalizadas en la comuna 1 son: "+str(suma))
        print("-----------------------------------------------")
        
        # g. Cantidad de obras “Finalizadas” en un plazo menor o igual a 24 meses
        query = Obra.select(fn.COUNT()).where(Obra.etapa_id == 'Finalizada' and Obra.plazo_meses <= 24)
        count = query.scalar()
        print("la cantidad de obras finalizadas en un plazo menor o igual a 24 meses son: "+str(count))
        print("-----------------------------------------------")

            
            
        
