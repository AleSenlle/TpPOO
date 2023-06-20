from peewee import *
from gestionar_obras import *

sqlite_db=GestionarObra().conectar_db()
#Punto 5
class Obra():

    def __init__(self, entorno: str, nombre: str, etapa: str, tipo_obra: str, area_responsable: str, descripcion: str, monto_contrato: float, barrio: str, direccion: str,  plazo_meses: int, beneficiarios: str, tipo_contratacion="0", nro_contratacion="0", mano_obra="0", destacada=0, expediente_numero="0", fuente_financiamiento ="0", fecha_inicio="0", fecha_fin_inicial="0", porcentaje_avance = 0, empresa="0", licitacion_anio="0"):
        self.entorno = entorno
        self.nombre = nombre
        self.etapa = etapa
        self.tipo_obra = tipo_obra
        self.area_responsable = area_responsable
        self.descripcion = descripcion
        self.monto_contrato = monto_contrato
        self.barrio = barrio
        self.direccion = direccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.plazo_meses = plazo_meses
        self.porcentaje_avance = porcentaje_avance
        #self.empresa = empresa
        self.licitacion_anio = licitacion_anio
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
        self.beneficiarios = beneficiarios
        self.mano_obra = mano_obra
        
        self.expediente_numero = expediente_numero
        self.fuente_financiamiento = fuente_financiamiento

        print("obra creada")

    @property
    def entorno(self):
        return self.__entorno

    @entorno.setter
    def entorno(self, value):
        self.__entorno = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def etapa(self):
        return self.__etapa

    @etapa.setter
    def etapa(self, value):
        self.__etapa = value

    @property
    def tipo_obra(self):
        return self.__tipo_obra

    @tipo_obra.setter
    def tipo_obra(self, value):
        self.__tipo_obra = value

    @property
    def area_responsable(self):
        return self.__area_responsable

    @area_responsable.setter
    def area_responsable(self, value):
        self.__area_responsable = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    @property
    def monto_contrato(self):
        return self.__monto_contrato

    @monto_contrato.setter
    def monto_contrato(self, value):
        self.__monto_contrato = value

    @property
    def barrio(self):
        return self.__barrio

    @barrio.setter
    def barrio(self, value):
        self.__barrio = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_fin_inicial(self):
        return self.__fecha_fin_inicial

    @fecha_fin_inicial.setter
    def fecha_fin_inicial(self, value):
        self.__fecha_fin_inicial = value

    @property
    def plazo_meses(self):
        return self.__plazo_meses

    @plazo_meses.setter
    def plazo_meses(self, value):
        self.__plazo_meses = value

    @property
    def porcentaje_avance(self):
        return self.__porcentaje_avance

    @porcentaje_avance.setter
    def porcentaje_avance(self, value):
        self.__porcentaje_avance = value

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, value):
        self.__empresa = value

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, value):
        self.__empresa = value

    @property
    def licitacion_anio(self):
        return self.__licitacion_anio

    @licitacion_anio.setter
    def licitacion_anio(self, value):
        self.__licitacion_anio = value

    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion

    @tipo_contratacion.setter
    def tipo_contratacion(self, value):
        self.__tipo_contratacion = value

    @property
    def nro_contratacion(self):
        return self.__nro_contratacion

    @nro_contratacion.setter
    def nro_contratacion(self, value):
        self.__nro_contratacion = value

    @property
    def beneficiarios(self):
        return self.__beneficiarios

    @beneficiarios.setter
    def beneficiarios(self, value):
        self.__beneficiarios = value

    @property
    def mano_obra(self):
        return self.__mano_obra

    @mano_obra.setter
    def mano_obra(self, value):
        self.__mano_obra = value

    @property
    def expediente_numero(self):
        return self.__expediente_numero

    @expediente_numero.setter
    def expediente_numero(self, value):
        self.__expediente_numero = value

    @property
    def destacada(self):
        return self.__destacada

    @destacada.setter
    def destacada(self, value):
        self.__destacada = value

    @property
    def fuente_financiamiento(self):
        return self.__fuente_financiamiento

    @fuente_financiamiento.setter
    def fuente_financiamiento(self, value):
        self.__fuente_financiamiento = value

    def __str__(self) -> str:
        
        

        return "el entorno es: " + str(self.entorno) + "\nEl nombre de la obra es: " + str(self.nombre) + "\nEstá en la etapa de: " + str(self.etapa) + "\nEl tipo de obra es: " + str(self.tipo_obra) + "\nEl área responsable es: " + str(self.area_responsable) + "\nLa descripción es: " + str(self.descripcion) + "\nEl monto del contrato es: " + str(self.monto_contrato) + "\nUbicada en el barrio de: " + str(self.barrio) + "\nLa dirección es: " + str(self.direccion) + "\nFecha de inicio: " + str(self.fecha_inicio) + "\nLa fecha prevista para la finalizacion es: " + str(self.fecha_fin_inicial) + "\nEl plazo de meses estimado es de: " + str(self.plazo_meses) + " meses" + "\nEl porcentaje de avance es de: " + str(self.porcentaje_avance) + "%" + "\nLa empresa a cargo es: " + str(self.empresa) + "\nLa licitación es del año: " + str(self.licitacion_anio) + "\nEl tipo de contratación es: " + str(self.tipo_contratacion) + "\nEl número de contratación es: " + str(self.nro_contratacion) + "\nLos beneficiarios son: " + str(self.beneficiarios) + "\nLa mano de obra está compuesta por: " + str(self.mano_obra) + " empleados" + "\nEl expediente es el número: " + str(self.expediente_numero) + " \n " + str(self.fuente_financiamiento) 

    def nuevo_proyecto(self):
         self.nombre=input("Ingrese el nombre del proyecto: ")
         self.etapa="proyecto"
         
        

    def iniciar_contratacion(self, tipo_contratacion: str, nro_contratacion):

        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
    
    def adjudicar_obra(self, empresa:str, expediente_numero:str):

        self.empresa = empresa
        self.expediente_numero = expediente_numero
    
   
    
    def iniciar_obra(self,fecha_inicio:str,fecha_fin_inicial,fuente_financiamiento:str,mano_obra:int):
       
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra

    def actualizar_porcentaje_avance(self,porc_incremento:int):
        self.porcentaje_avance =self.porcentaje_avance + porc_incremento
    
    def incrementar_plazo(self,meses:int):
        self.plazo_meses =self.plazo_meses + meses
    
    

    def incrementar_mano_obra(self, cantidad:int):
        self.mano_obra = self.mano_obra + cantidad

    def finalizar_obra(self, obj_etapa_fin):
        self.porcentaje_avance = 100
        self.etapa = obj_etapa_fin

    def rescindir_obra(self):
        self.etapa = 'Rescindida'


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
            expediente_numero = CharField()
            etapa = ForeignKeyField(Eetapas, backref='etapas')
            empresa = ForeignKeyField(Eempresa, backref='empresa')
            tipo_obra = ForeignKeyField(Etipo_obra, backref='tipo_obra')
            area_responsable = ForeignKeyField(Eareas_responsables, backref='areas_responsables')
            barrio = ForeignKeyField(Ebarrios, backref='barrios')
            tipo_contratacion = ForeignKeyField(Etipo_contratacion, backref='tipo_contratacion')
            #financiamiento = ForeignKeyField(EFinanciamiento, backref='financiamiento')
            class Meta:
                db_table = 'Obras Públicas'

          
lista=[Ebarrios,Eareas_responsables,Ecomunas,Eempresa,Eetapas,EstructuraBDObras,Etipo_obra,Etipo_contratacion,EFinanciamiento]
GestionarObra().mapear_orm(sqlite_db,lista)
class Obra ():
    def nuevo_proyecto():
        pass
    def iniciar_contratacion():
        pass

#GestionarObra().cargar_datos(Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,EstructuraBDObras)




