from __init__ import db


tiene = db.Table('tiene', db.metadata,  
        db.Column('id_replica_actual', db.Integer, db.ForeignKey('replica.id'), primary_key=True),
        db.Column('id_replica_siguiente', db.Integer, db.ForeignKey('replica.id'), primary_key=True))

class Replica(db.Model):
    __tablename__='replica'
    __table_args__ = {'mysql_engine':'InnoDB','mysql_charset':'utf8','mysql_collate':'utf8_general_ci'}

    id = db.Column(db.Integer,primary_key=True)
    apodo = db.Column(db.String(20))
    descripcion = db.Column(db.String(150))
    id_comentario = db.Column(db.Integer)
    rel = db.relationship('Replica', secondary=tiene, primaryjoin=tiene.c.id_replica_actual==id,
                    secondaryjoin=tiene.c.id_replica_siguiente==id)

    def __init__(self,apodo,descripcion,id_comentario) -> None:
        self.apodo = apodo
        self.descripcion = descripcion
        self.id_comentario = id_comentario
    
    def __repr__(self) -> str:
        return f'Id:{self.id} // Replica:{self.descripcion} // {self.rel}'
