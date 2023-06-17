from peewee import*
import pandas as pd
from abc import ABCMeta
import os


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
    
    #Este es el punto 4.e
    @classmethod
    def cargar_datos(self,Ecomunas):
        df=self.limpiar_datos()
        data_unique = list(df['comuna'].unique())
        print(data_unique)
        for elem in data_unique:
            print("Elemento:", elem)
            try:
                Ecomunas.create(nro_comuna=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla tipos_transporte.", e)
        print("Se han persistido los tipos de transporte en la BD.")
            

    
        
    
    
                