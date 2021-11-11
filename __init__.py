from flask import Flask,render_template,flash,g,redirect,request,session,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)
db.init_app(app)

class Comentario(db.Model):
    __tablename__='comentario'

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

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route("/<int:id_contenido>/nuevoComentario",methods=['GET','POST'])
def comentario(id_contenido):
    if request.method == 'POST':
        print( request.form.get('apodo'))
        apodo = request.form.get('apodo')
        titulo= request.form.get('titulo')
        detalle = request.form.get('detalle')
        print("pepepe")
        newComment = Comentario(apodo,titulo,detalle,id_contenido)  
        print(newComment.titulo)  
        db.session.add(newComment)
        db.session.commit()
        print("se guardo el comentario")
        print(newComment.id)
        print(Comentario.query.all())

    return render_template('nuevoComentario.html',id_contenido=id_contenido)

