from peewee import *
import os
import pandas as pd

sqlite_db = SqliteDatabase(os.getcwd()+'/'+'obras_urbanas.db', pragmas={'journal_mode': 'wal'})

try:
    sqlite_db.connect()
    #La base de datos se crea cuando intenta conectarse por primera vez y no la encuentra.
except OperationalError as e:
    print("Se ha generado un error en la conexion a la BD.", e)
    exit()

class BaseModel(Model):
    class Meta:
        database=sqlite_db
class EstructuraBDObras (BaseModel):
    entorno=CharField()
    nombre=CharField()
    etapa=CharField()
    tipo=CharField()
    area_responsable=CharField()
    descripcion=CharField()
    monto_contrato=CharField()
    comuna=CharField()
    barrio=CharField()
    direccion=CharField()
    lat=CharField()
    lng=CharField()
    fecha_inicio=CharField()
    fecha_fin_inicial=CharField()
    plazo_meses=CharField()
    porcentaje_avance=CharField()
    imagen_1=CharField()
    imagen_2=CharField()
    imagen_3=CharField()
    imagen_4=CharField()
    licitacion_oferta_empresa=CharField()
    licitacion_anio=CharField()
    contratacion_tipo=CharField()
    nro_contratacion=CharField()
    cuit_contratista=CharField()
    beneficiarios=CharField()
    mano_obra=CharField()
    compromiso=CharField()
    destacada=CharField()
    ba_elige=CharField()
    link_entorno=CharField()
    pliego_descarga=CharField()
    expediente_numero=CharField()
    estudio_ambiental_descarga=CharField()
    financiamiento=CharField()
    class Meta:
        db_table='Obras Públicas'
sqlite_db.create_tables([EstructuraBDObras])

def importar_datos_csv():
    """Archivo con obras publicas de la ciudad."""
    
    archivo_csv = os.getcwd()+"/"+"observatorio-de-obras-urbanas.csv"
    #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"

    try:
        df = pd.read_csv(archivo_csv, sep=",")
        return df
    except FileNotFoundError as e:
        print("Error al conectar con el dataset.", e)
        return False

if __name__== "__main__" :
    df = importar_datos_csv()
    if df is False:
        exit()
#Obtenemos información sobre la estructura del archivo csv
    print(df.head())
    print(df.count())
    print(df.columns)