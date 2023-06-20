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
    def cargar_datos(self,Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,Eimagen,EstructuraBDObras):
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
        df.drop_duplicates(subset=['barrio'],inplace=True)
        df.drop_duplicates(subset=['licitacion_oferta_empresa'],inplace=True)
        #df.drop_duplicates(subset=['imagen'],inplace=True)
        df.drop_duplicates(subset=['nombre'],inplace=True)
        df.drop_duplicates(subset=['descripcion'],inplace=True)
                           #,'nombre','etapa', 'tipo', 'area_responsable', 'descripcion', 'monto_contrato', 'comuna', 'barrio', 'direccion', 'lat', 'lng', 'fecha_inicio', 'fecha_fin_inicial', 'plazo_meses', 'porcentaje_avance', 'imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 'licitacion_oferta_empresa', 'licitacion_anio', 'contratacion_tipo', 'nro_contratacion', 'cuit_contratista', 'beneficiarios', 'mano_obra', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'pliego_descarga', 'expediente-numero', 'estudio_ambiental_descarga', 'financiamiento'])
        for elem in df.values:
           if elem is not np.nan:
                print(elem)
                try:
                    Eempresa.create(cuit=elem[25], razonSocial=elem[21])
                    Ebarrios.create(nombre=elem[9],nro_comuna=elem[8])
                    EstructuraBDObras.create(entorno=elem[2],nombre=elem[3],descripcion=elem[7],monto_contrato=elem[8],direccion=elem[11],fecha_inicio=elem[14],fecha_fin_inicial=elem[15],plazo_meses=elem[16],porcentaje_avance=0.0,licitacion_anio=elem[23],nro_contratacion=elem[25],beneficiarios=elem[27],mano_obra=elem[28],destacada=elem[30],expediente_numero=elem[34])

                    #Eimagen.create(id_obra_id=elem[])
                except IntegrityError as e:
                    print("Error al insertar un nuevo registro en la tabla Empresa.", e)
        print("Se han persistido los tipos de Empresas en la BD.")
    

    
                