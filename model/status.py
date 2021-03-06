
from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase, Check

db = SqliteDatabase('wgpark.db')

class StatusModel(Model):

    pkcodstatus = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False, unique=True)
    
    class Meta:
        database = db
        table_name = 'TB_StatusModel'
        constraints=[Check("descricao = upper('o') OR descricao = upper('c')")]

    def create_status(self):

        try:
            self.save(force_insert=True)
            return True

        except:
            return None
    
    @classmethod
    def read_status_list(cls):

        status = cls.select()
        
        if status:
            return status
            
        return None

    @classmethod
    def read_status_before_post(cls, descricao):

        status = cls.get_or_none(cls.descricao == descricao)
        if status:
            return status
            
        return None

    @classmethod
    def read_status(cls, pkcodstatus):

        status = cls.get_or_none(cls.pkcodstatus == pkcodstatus)

        if status:
            return status
            
        return None
            
    def delete_status(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodstatus': self.pkcodstatus,
                'descricao': self.descricao
               }
