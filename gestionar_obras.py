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
        class Ebarrios (BaseModel):
            id = IntegerField(primary_key=True)
            nombre = CharField()
            nro_comuna = IntegerField()
            class Meta:
                db_table = 'barrios'

        class Eareas_responsables (BaseModel):
            id = IntegerField(primary_key=True)
            descripcion = CharField()
            class Meta:
                db_table = 'areas_responsables'
        
        class Ecomunas (BaseModel):
            id = IntegerField(primary_key=True)
            nro_comuna = IntegerField()
            class Meta:
                db_table = 'comunas'
        
        class Eempresa (BaseModel):
            id = IntegerField(primary_key=True)
            cuit = CharField()
            razonSocial = CharField()
            class Meta:
                db_table = 'empresa'
        
        class Eetapas (BaseModel):
            id = IntegerField(primary_key=True)
            descripcion = CharField()
            class Meta:
                db_table = 'etapas'
        
        class EFuenteFinanciamiento (BaseModel):
            id = IntegerField(primary_key=True)
            descripcion = CharField()
            class Meta:
                db_table = 'fuente_financiamiento'
        
       
        
        class Etipo_contratacion (BaseModel):
            id = IntegerField(primary_key=True)
            descripcion = CharField()
            class Meta:
                db_table = 'tipo_contratacion'
        
        class Etipo_obra (BaseModel):
            id = IntegerField(primary_key=True)
            descripcion = CharField()
            class Meta:
                db_table = 'tipo_obra'  
            
        
        class EstructuraBDObras (BaseModel):
            id = IntegerField(primary_key=True)    
            entorno = CharField()
            nombre = CharField()
            descripcion = CharField()
            monto_contrato = IntegerField()
            direccion = CharField()
            fecha_inicio = DateField()
            fecha_fin_inicial = DateField()
            plazo_meses = IntegerField()
            porcentaje_avance = IntegerField()
            licitacion_ano = IntegerField()
            nro_contratacion = CharField()
            beneficiarios = CharField()
            mano_obra = CharField()
            destacada = CharField()
            expediente_numero = CharField()
            id_etapa = ForeignKeyField(Eetapas, backref='etapas')
            id_empresa = ForeignKeyField(Eempresa, backref='empresa')
            id_tipo_obra = ForeignKeyField(Etipo_obra, backref='tipo_obra')
            id_areas_responsables = ForeignKeyField(Eareas_responsables, backref='areas_responsables')
            id_barrio = ForeignKeyField(Ebarrios, backref='barrios')
            id_tipo_contratacion = ForeignKeyField(Etipo_contratacion, backref='tipo_contratacion')
            id_fuente_financiamiento = ForeignKeyField(EFuenteFinanciamiento, backref='fuente_financiamiento')
            
            class Meta:
                db_table = 'Obras Públicas'
        class Eimagen (BaseModel):
            id = IntegerField(primary_key=True)
            id_obra = ForeignKeyField(EstructuraBDObras, backref='obra')
            descripcion = CharField()
            class Meta:
                db_table = 'imagen'
                
        sqlite_db.create_tables([EstructuraBDObras,Ebarrios,Eareas_responsables,Ecomunas,Eempresa,Eetapas,EFuenteFinanciamiento,Eimagen,Etipo_contratacion,Etipo_obra])
        return EstructuraBDObras
    
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
    
    
        
    
    
                