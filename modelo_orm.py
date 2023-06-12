from peewee import *
from gestionar_obras import *

sqlite_db = GestionarObra().conectar_db()
class BaseModel(Model):

    class Meta:
        database = sqlite_db
GestionarObra().mapear_orm(BaseModel,sqlite_db)







