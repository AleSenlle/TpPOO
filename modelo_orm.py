from peewee import *
import os
from gestionar_obras import *

sqlite_db=GestionarObra().conectar_db()
class BaseModel(Model):
    class Meta:
        database=GestionarObra().conectar_db()
               
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

class Obra ():
    def nuevo_proyecto():
        pass
    def iniciar_contratacion():
        pass






