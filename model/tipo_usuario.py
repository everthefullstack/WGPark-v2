
from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase

db = SqliteDatabase('wgpark.db')

class TipoUsuarioModel(Model):

    pkcodtipo = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False, unique=True)
    
    class Meta:
        database = db
        table_name = 'TB_TipoUsuarioModel'

    def create_tipo(self):

        try:
            self.save(force_insert=True)
            return True
        
        except:
            return None
    
    @classmethod
    def read_tipos(cls):

        tipos = cls.select()
        if tipos:
            return tipos
            
        return None

    @classmethod
    def read_tipo_usuario_before_post(cls, descricao):

        tipo_usuario = cls.get_or_none(cls.descricao == descricao)
        if tipo_usuario:
            return tipo_usuario
            
        return None

    @classmethod
    def read_tipo(cls, pkcodtipo):

        tipo_usuario = cls.get_or_none(cls.pkcodtipo == pkcodtipo)
        if tipo_usuario:
            return tipo_usuario
            
        return None

    def update_tipo(self, pkcodtipo):

        try:
            self.descricao = descricao
            self.save()
        except:
            return None
            
    def delete_tipo(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodtipo': self.pkcodtipo,
                'descricao': self.descricao
               }
