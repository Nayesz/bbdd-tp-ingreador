from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

USER = 'root'
PASS= 'root'
URL= 'localhost:3306'
NAME = 'contentappdb'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'''mysql://{USER}:
                        {PASS}@{URL}/{NAME}'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


migrate = Migrate()
migrate.init_app(app, db)

class Comentario(db.Model):
    id_comentario = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(45))
    descripcion = db.Column(db.String(280))
    apodo_comentarista = db.Column(db.String(20))

    def __str__(self):
        return f'''ID: {self.id_comentario}, titulo: {self.titulo}, 
                descripcion: {self.descripcion}, 
                apodo_comentarista: {self.apodo_comentarista}'''

class Replica(db.Model):
    id_replica = db.Column(db.Integer, primary_key=True)
    detalle = db.Column(db.String(280))
    apodo_replica = db.Column(db.String(20))
    id_comentario = db.Column(db.Integer)

    def __str__(self):
        return f'''ID: {self.id_replica}, detalle: {self.detalle}, 
                apodo_replica: {self.apodo_replica},  
                id_comentario: {self.id_comentario}'''
        

@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)