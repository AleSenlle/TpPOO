from peewee import *
from gestionar_obras import *

sqlite_db=GestionarObra().conectar_db()
class BaseModel(Model):

    class Meta:
        database = sqlite_db
class Ebarrios (BaseModel):
            nombre = CharField()
            nro_comuna = IntegerField()
            class Meta:
                db_table = 'barrios'

class Eareas_responsables (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'areas_responsables'
class Ecomunas (BaseModel):
            nro_comuna = IntegerField()
            class Meta:
                db_table = 'comunas'
        
class Eempresa (BaseModel):
            cuit = CharField()
            razonSocial = CharField()
            class Meta:
                db_table = 'empresa'
        
class Eetapas (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'etapas'
        
class EFuenteFinanciamiento (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'fuente_financiamiento'
        
       
        
class Etipo_contratacion (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'tipo_contratacion'
        
class Etipo_obra (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'tipo_obra'  
            
        
class EstructuraBDObras (BaseModel):    
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
            id_obra = ForeignKeyField(EstructuraBDObras, backref='obra')
            descripcion = CharField()
            class Meta:
                db_table = 'imagen'
lista=[Ebarrios,Eareas_responsables,Ecomunas,Eempresa,Eetapas,Eimagen,EstructuraBDObras,Etipo_obra,Etipo_contratacion,EFuenteFinanciamiento]
GestionarObra().mapear_orm(sqlite_db,lista)
class Obra ():
    def nuevo_proyecto():
        pass
    def iniciar_contratacion():
        pass


GestionarObra().cargar_datos(Ecomunas)





