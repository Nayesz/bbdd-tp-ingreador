from __init__ import db

class Comentario(db.Model):
    __tablename__='comentario'
    __table_args__ = {'mysql_engine':'InnoDB','mysql_charset':'utf8','mysql_collate':'utf8_general_ci'}

    id = db.Column(db.Integer,primary_key=True)
    apodo = db.Column(db.String(20))
    titulo =db.Column(db.String(20))
    descripcion = db.Column(db.String(50))
    id_contenido = db.Column(db.Integer)

    def __init__(self,apodo,titulo,descripcion,id_contenido) -> None:
        self.apodo = apodo
        self.titulo =titulo
        self.descripcion = descripcion
        self.id_contenido = id_contenido
    
    def __repr__(self) -> str:
        return f'Id:{self.id} // Comentario:{self.descripcion}'

