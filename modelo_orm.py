from peewee import *
from gestionar_obras import *

sqlite_db=GestionarObra().conectar_db()
class BaseModel(Model):

    class Meta:
        database = sqlite_db

class Eareas_responsables (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'area_responsable'
                
class Ecomunas (BaseModel):
            nro_comuna = IntegerField()
            class Meta:
                db_table = 'comunas'

class Ebarrios (BaseModel):
            nombre = CharField()
            nro_comuna = ForeignKeyField(Ecomunas,backref='comunas')
            class Meta:
                db_table = 'barrios'
        
class Eempresa (BaseModel):
            cuit = CharField()
            razonSocial = CharField()
            class Meta:
                db_table = 'empresa'
        
class Eetapas (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'etapas'
        
class EFinanciamiento (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'financiamiento'    
        
class Etipo_contratacion (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'contratacion_tipo'
        
class Etipo_obra (BaseModel):
            descripcion = CharField()
            class Meta:
                db_table = 'tipo'  
        
class EstructuraBDObras (BaseModel):    
            entorno = CharField()
            nombre = CharField()
            descripcion = CharField()
            monto_contrato = IntegerField()
            direccion = CharField()
            fecha_inicio = DateField()
            fecha_fin_inicial = DateField()
            plazo_meses = IntegerField()
            porcentaje_avance = DoubleField(default=0.0)
            licitacion_anio = DateField()
            nro_contratacion = CharField()
            beneficiarios = CharField()
            mano_obra = CharField()
            destacada = CharField()
            expediente_numero = CharField()
            class Meta:
                db_table = 'Obras Públicas'
'''           etapa = ForeignKeyField(Eetapas, backref='etapas')
            empresa = ForeignKeyField(Eempresa, backref='empresa')
            tipo_obra = ForeignKeyField(Etipo_obra, backref='tipo_obra')
            areas_responsables = ForeignKeyField(Eareas_responsables, backref='areas_responsables')
            barrio = ForeignKeyField(Ebarrios, backref='barrios')
            tipo_contratacion = ForeignKeyField(Etipo_contratacion, backref='tipo_contratacion')
            financiamiento = ForeignKeyField(EFinanciamiento, backref='financiamiento')'''
            
           

class Eimagen (BaseModel):
            id_obra = ForeignKeyField(EstructuraBDObras, backref='obra')
            descripcion = CharField()
            class Meta:
                db_table = 'imagen'

lista=[Ebarrios,Eareas_responsables,Ecomunas,Eempresa,Eetapas,Eimagen,EstructuraBDObras,Etipo_obra,Etipo_contratacion,EFinanciamiento]
GestionarObra().mapear_orm(sqlite_db,lista)
class Obra ():
    def nuevo_proyecto():
        pass
    def iniciar_contratacion():
        pass

GestionarObra().cargar_datos(Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,Eimagen,EstructuraBDObras)





