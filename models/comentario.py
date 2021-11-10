from __init__ import db

class Comentario(db.Model):
    __tablename__='comentario'

    id = db.Column(db.Integer,primary_key=True)
    apodo = db.Column(db.String(20))
    titulo =db.Column(db.String(20))
    descripcion = db.Column(db.String(50))
    id_contenido = db.Column(db.Integer)

    def __init__(self,apodo,titulo,descripcion,id_comentario) -> None:
        self.apodo = apodo
        self.titulo =titulo
        self.descripcion = descripcion
        self.id_contenido = id_contenido
    
    def __repr__(self) -> str:
        return f'Id:{self.id} // Comentario:{self.descripcion}'

