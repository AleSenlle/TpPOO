from peewee import *
from gestionar_obras import *


sqlite_db = GestionarObra().conectar_db()


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
    nro_comuna = ForeignKeyField(Ecomunas, backref='comunas')

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


class Obra (BaseModel):
    entorno = CharField()
    nombre = CharField()
    descripcion = CharField()
    monto_contrato = IntegerField()
    direccion = CharField()
    fecha_inicio = DateField(default='0/0/0000')
    fecha_fin_inicial = DateField(default='0/0/0000')
    plazo_meses = IntegerField()
    porcentaje_avance = DoubleField(default=0.0)
    licitacion_anio = DateField(default='0/0/0000')
    nro_contratacion = CharField(default='0')
    beneficiarios = CharField()
    mano_obra = CharField(default='0')
    expediente_numero = CharField(default='0')
    etapa = ForeignKeyField(Eetapas, backref='etapas')
    empresa = ForeignKeyField(Eempresa, backref='empresa')
    tipo_obra = ForeignKeyField(Etipo_obra, backref='tipo_obra')
    area_responsable = ForeignKeyField(
        Eareas_responsables, backref='areas_responsables')
    barrio = ForeignKeyField(Ebarrios, backref='barrios')
    tipo_contratacion = ForeignKeyField(
        Etipo_contratacion, backref='tipo_contratacion')
    financiamiento = CharField()
    

    class Meta:
        db_table = 'Obras_publicas'

    def __str__(self) -> str:
        return "el entorno es: " + str(self.entorno) + "\nEl nombre de la obra es: " + str(self.nombre) + "\nEstá en la etapa de: " + str(self.etapa) + "\nEl tipo de obra es: " + str(self.tipo_obra) + "\nEl área responsable es: " + str(self.area_responsable) + "\nLa descripción es: " + str(self.descripcion) + "\nEl monto del contrato es: " + str(self.monto_contrato) + "\nUbicada en el barrio de: " + str(self.barrio) + "\nLa dirección es: " + str(self.direccion) + "\nFecha de inicio: " + str(self.fecha_inicio) + "\nLa fecha prevista para la finalizacion es: " + str(self.fecha_fin_inicial) + "\nEl plazo de meses estimado es de: " + str(self.plazo_meses) + " meses" + "\nEl porcentaje de avance es de: " + str(self.porcentaje_avance) + "%" + "\nLa empresa a cargo es: " + str(self.empresa) + "\nLa licitación es del año: " + str(self.licitacion_anio) + "\nEl tipo de contratación es: " + str(self.tipo_contratacion) + "\nEl número de contratación es: " + str(self.nro_contratacion) + "\nLos beneficiarios son: " + str(self.beneficiarios) + "\nLa mano de obra está compuesta por: " + str(self.mano_obra) + " empleados" + "\nEl expediente es el número: " + str(self.expediente_numero) + " \n " + str(self.fuente_financiamiento)

    def nuevo_proyecto(self):
        self.nombre = input("Ingrese el nombre del proyecto: ")
        self.etapa = "Proyecto"

    def iniciar_contratacion(self, tipo_contratacion: str, nro_contratacion):

        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion

    def adjudicar_obra(self, empresa: str, expediente_numero: str):

        self.empresa = empresa
        self.expediente_numero = expediente_numero

    def iniciar_obra(self, fecha_inicio: str, fecha_fin_inicial, fuente_financiamiento: str, mano_obra: int):

        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra

    def actualizar_porcentaje_avance(self, porc_incremento: int):
        self.porcentaje_avance = self.porcentaje_avance + porc_incremento

    def incrementar_plazo(self, meses: int):
        self.plazo_meses = self.plazo_meses + meses

    def incrementar_mano_obra(self, cantidad: int):
        self.mano_obra = self.mano_obra + cantidad

    def finalizar_obra(self, obj_etapa_fin):
        self.porcentaje_avance = 100
        self.etapa = obj_etapa_fin

    def rescindir_obra(self):
        self.etapa = 'Rescindida'


lista = [Ebarrios, Eareas_responsables, Ecomunas, Eempresa,
         Eetapas, Obra, Etipo_obra, Etipo_contratacion, EFinanciamiento]
#GestionarObra().mapear_orm(sqlite_db,lista)
#GestionarObra().cargar_datos(Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,Obra)

obra = GestionarObra().nueva_obra(Obra, Etipo_obra, Eareas_responsables, Ebarrios, Eetapas)
#GestionarObra().obtener_indicadores(Obra,Etipo_obra,Eareas_responsables, Ebarrios, Eetapas)