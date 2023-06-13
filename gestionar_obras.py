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
    def mapear_orm(self,BaseModel,sqlite_db):
        class EstructuraBDObras (BaseModel):
            entorno = CharField()
            nombre = CharField()
            etapa = CharField()
            tipo = CharField()
            area_responsable = CharField()
            descripcion = CharField()
            monto_contrato = CharField()
            comuna = CharField()
            barrio = CharField()
            direccion = CharField()
            lat = CharField()
            lng = CharField()
            fecha_inicio = CharField()
            fecha_fin_inicial = CharField()
            plazo_meses = CharField()
            porcentaje_avance = CharField()
            imagen_1 = CharField()
            imagen_2 = CharField()
            imagen_3 = CharField()
            imagen_4 = CharField()
            licitacion_oferta_empresa = CharField()
            licitacion_anio = CharField()
            contratacion_tipo = CharField()
            nro_contratacion = CharField()
            cuit_contratista = CharField()
            beneficiarios = CharField()
            mano_obra = CharField()
            compromiso = CharField()
            destacada = CharField()
            ba_elige = CharField()
            link_entorno = CharField()
            pliego_descarga = CharField()
            expediente_numero = CharField()
            estudio_ambiental_descarga = CharField()
            financiamiento = CharField()

            class Meta:
                db_table = 'Obras Públicas'
        sqlite_db.create_tables([EstructuraBDObras])
                
                