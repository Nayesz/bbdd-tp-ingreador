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

@app.route("/<int:id_comentario>/borrarComentario",methods=['GET','DELETE'])
def borrarComentario(id_comentario):
        comentario= Comentario.query.filter_by(id=id_comentario).first()
        id_contenidop=comentario.id_contenido
        db.session.delete(comentario)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = id_contenidop))

@app.route("/<int:id_comentario>/editarComentario",methods=['GET','POST'])
def editarComentario(id_comentario):
        _comentario= Comentario.query.filter_by(id=id_comentario).first()
        if request.method == 'POST':
            _comentario.titulo= request.form.get('titulo')
            _comentario.descripcion = request.form.get('descripcion')
            db.session.add(_comentario)
            db.session.commit()
            return redirect(url_for('obtenerComentario', _id_contenido = _comentario.id_contenido))

        return render_template('editarComentario.html',comentario=_comentario)

        id_contenidop=comentario.id_contenido

        db.session.delete(comentario)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = id_contenidop))


#TO-DO cobrar el cheque en blanco A GONZA

@app.route("/<int:id_contenido>/nuevoComentario",methods=['GET','POST'])
def comentario(id_contenido):
    if request.method == 'POST':
        apodo = request.form.get('apodo')
        titulo= request.form.get('titulo')
        detalle = request.form.get('detalle')
        newComment = Comentario(apodo,titulo,detalle,id_contenido)  
        db.session.add(newComment)
        db.session.commit()

    return render_template('nuevoComentario.html',id_contenido=id_contenido)


@app.route("/<int:_id_contenido>/obtenerComentario",methods=['GET'])
def obtenerComentario(_id_contenido):
        comentarios= Comentario.query.filter_by(id_contenido=_id_contenido)
        print(comentarios)
        return render_template('mostrarComentarios.html',comentarios=comentarios)


