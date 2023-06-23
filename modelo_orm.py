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
        self.etapa = 'Proyecto'
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")
        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Etipo_obra.select().where(Etipo_obra.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("los tipos de obras son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 25:
                try:
                    self.tipo_obra = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 24")
                opcion_elegida = int(input("Elija el número de opción: "))
        print("-----------------------------------------------")
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")

        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Eareas_responsables.select().where(
            Eareas_responsables.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("las areas responsables son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 21:
                try:
                    area_responsable = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 20")
                opcion_elegida = int(input("Elija el número de opción: "))
                # Consulta a la base de datos
        
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")
        query = Ebarrios.select().where(Ebarrios.nombre != ' ')
        resultados = list(query)
        print("los barrios son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.nombre)
            i = i+1
            lista.append(resultado.nombre)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 57:
                try:
                    self.barrio = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 56")
                opcion_elegida = int(input("Elija el número de opción: "))


    def iniciar_contratacion(self):
        
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")
        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Etipo_contratacion.select().where(Etipo_contratacion.descripcion != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("los tipos de contratacion son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 43:
                try:
                    self.tipo_contratacion = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 43")
                opcion_elegida = int(input("Elija el número de opción: "))
        print("-----------------------------------------------")
        self.nro_contratacion = int(input("Ingrese el número de contratación: "))

        

    def adjudicar_obra(self):
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")
        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = Eempresa.select().where(
            Eempresa.razonSocial != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("los tipos de obras son:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.razonSocial)
            i = i+1
            lista.append(resultado.razonSocial)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 387:
                try:
                    self.empresa = lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 386")
                opcion_elegida = int(input("Elija el número de opción: "))
        print("-----------------------------------------------")
        self.expediente_numero = int(input("Ingrese el número de expediente: "))

        

    def iniciar_obra(self):

        self.fecha_inicio = input("Ingrese la fecha de inicio: ")
        self.fecha_fin_inicial = input("Ingrese la fecha estimada de fin: ")
        
        sqlite_db = GestionarObra().conectar_db()

        print("Conexión exitosa a la base de datos")
        print("-----------------------------------------------")
        # Consulta a la base de datos
        query = EFinanciamiento.select().where(
            EFinanciamiento.razonSocial != ' ')
        resultados = list(query)

        # Recorre los resultados y muestra la descripción
        print("las fuentes de financiamiento:")
        print("-----------------------------------------------")
        i = 1
        lista = []
        for resultado in resultados:
            print(str(i)+" "+resultado.descripcion)
            i = i+1
            lista.append(resultado.descripcion)

        sqlite_db.close()
        print("-----------------------------------------------")

        opcion_elegida = int(input("Elija el número de opción: "))
        while True:
            if opcion_elegida > 0 and opcion_elegida < 10:
                try:
                    self.financiamiento= lista[opcion_elegida-1]

                except:
                    print("ingrese una opcion correcta")

                break
            else:
                print("Ingrese un número entre 1 y 9")
                opcion_elegida = int(input("Elija el número de opción: "))
        print("-----------------------------------------------")
        self.mano_obra = int(input("Ingrese la cantidad de mano de obra: "))
    
    def actualizar_porcentaje_avance(self):
        self.porcentaje_avance =self.porcentaje_avance+ int(input("Ingrese el porcentaje de avance: "))

    def incrementar_plazo(self):
        self.plazo_meses =self.plazo_meses+ int(input("Ingrese la cantidad de meses a incrementar: "))

    def incrementar_mano_obra(self):
        self.mano_obra = self.mano_obra + int(input("Ingrese la cantidad de mano de obra a incrementar: "))

    def finalizar_obra(self, obj_etapa_fin):
        self.porcentaje_avance = 100
        self.etapa = "Finalizada"

    def rescindir_obra(self):
        self.etapa = 'Rescindida'


#lista = [Ebarrios, Eareas_responsables, Ecomunas, Eempresa,
#         Eetapas, Obra, Etipo_obra, Etipo_contratacion, EFinanciamiento]
#GestionarObra().mapear_orm(sqlite_db,lista)
#GestionarObra().cargar_datos(Ecomunas,Eareas_responsables,Eetapas,EFinanciamiento,Etipo_contratacion,Etipo_obra,Eempresa,Ebarrios,Obra)

#obra = GestionarObra().nueva_obra(Obra, Etipo_obra, Eareas_responsables, Ebarrios, Eetapas)
#GestionarObra().obtener_indicadores(Obra,Etipo_obra,Eareas_responsables, Ebarrios, Eetapas)

