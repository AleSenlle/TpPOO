from peewee import*
import pandas as pd
from abc import ABCMeta
import os
import numpy as np


class GestionarObra(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    #Este es el punto 4.A
    @classmethod
    def extraer_datos(self):
        try:
            archivo_csv = os.getcwd()+"/"+"observatorio-de-obras-urbanas.csv"
            df = pd.read_csv(archivo_csv, sep=",")
            return df
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return False

    #Este es el punto 4.B
    @classmethod
    def conectar_db(self):
        sqlite_db = SqliteDatabase(os.getcwd()+'/'+'obras_urbanas.db', pragmas={'journal_mode': 'wal'})
        try:
            sqlite_db.connect()
            #La base de datos se crea cuando intenta conectarse por primera vez y no la encuentra.
            return sqlite_db
        except OperationalError as e:
            print("Se ha generado un error en la conexion a la BD.", e)
            exit()

    #Este es el punto 4.C
    @classmethod
    def mapear_orm(self,sqlite_db,lista):
        sqlite_db.create_tables(lista)
        
    #Este es el punto 4.D
    @classmethod
    def limpiar_datos(self):
        df=self.extraer_datos()
        print(df)
        print("limpiando datos")
        df.dropna(subset=["monto_contrato", "comuna", "barrio", "direccion","etapa", "tipo", "area_responsable", "descripcion",
                  ], axis=0, inplace=True)
        print(df)
        return df
    
    #Este es el punto 4.E
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
    def cargar_datos(self,Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,EstructuraBDObras):
        df=self.limpiar_datos()
       
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
                print("Error al insertar un nuevo registro en la tabla Area Responsable.", e)
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
                    print("Error al insertar un nuevo registro en la tabla Financiamiento.", e)
        print("Se han persistido los tipos de Obras en la BD.")

        data_unique = list(df['contratacion_tipo'].unique())
        print(data_unique)
        for elem in data_unique:
            if elem is not np.nan:
                print("Elemento:", elem)
                try:
                    Etipo_contratacion.create(descripcion=elem)
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla Tipo de Contratacion.", e)
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
         
         #Ahora normalizo las tablas que tienen +2 columnas:                   
        df.drop_duplicates(subset=['nombre'],inplace=True)
        for elem in df.values:
           if elem is not np.nan:
                try:
                    EstructuraBDObras.create(entorno=elem[1],nombre=elem[2],descripcion=elem[6],monto_contrato=elem[7],direccion=elem[10],fecha_inicio=elem[13],fecha_fin_inicial=elem[14],plazo_meses=elem[15],porcentaje_avance=0.0,licitacion_anio=elem[22],nro_contratacion=elem[24],beneficiarios=elem[26],mano_obra=elem[27],expediente_numero=elem[33],etapa=elem[3],empresa=elem[21],tipo_obra=elem[4],area_responsable=elem[5],barrio=elem[9],tipo_contratacion=elem[23])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla obras.", e)
        print("Se han persistido las obras en la BD.")
           
        df.drop_duplicates(subset=['licitacion_oferta_empresa'],inplace=True)
        for elem in df.values:
           if elem is not np.nan:
                print(elem)
                try:
                    Eempresa.create(cuit=elem[25], razonSocial=elem[21])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla Empresa.", e)
        print("Se han persistido los tipos de Empresas en la BD.")
    
        df.drop_duplicates(subset=['barrio'],inplace=True)                   
        for elem in df.values:
           if elem is not np.nan:
                print(elem)
                try:
                    Ebarrios.create(nombre=elem[9],nro_comuna=elem[8])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla barrio.", e)
        print("Se han persistido los barrios en la BD.")
                