from flask import Flask,render_template,flash,g,redirect,request,session,url_for
from db import db
from models.comentario import Comentario
from models.replica import Replica, tiene

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/')
def routeador():
    return redirect(url_for('home'))


@app.route("/contenido",methods=['GET'])
def home():
    func()
    return render_template("home.html")

@app.route("/contenido/<int:_id_contenido>/comentario/",methods=['GET'])
def obtenerComentario(_id_contenido):
    comentarios= Comentario.query.filter_by(id_contenido=_id_contenido)
    #print(comentarios)
    return render_template('mostrarComentarios.html',comentarios=comentarios, id = _id_contenido)

@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/delete",methods=['GET','DELETE'])
def borrarComentario(_id_contenido, id_comentario):
    comentario= Comentario.query.filter_by(id=id_comentario).first()
    db.session.delete(comentario)
    db.session.commit()
    return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))


@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/update",methods=['GET','POST'])
def editarComentario(_id_contenido, id_comentario):
    _comentario= Comentario.query.filter_by(id=id_comentario).first()
    if request.method == 'POST':
        _comentario.titulo= request.form.get('titulo')
        _comentario.descripcion = request.form.get('descripcion')
        db.session.add(_comentario)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))
    return render_template('editarComentario.html', comentario=_comentario)


@app.route("/contenido/<int:_id_contenido>/comentario/create",methods=['GET','POST'])
def crearComentario(_id_contenido):
    if request.method == 'POST':
        apodo = request.form.get('apodo')
        titulo= request.form.get('titulo')
        detalle = request.form.get('descripcion')
        newComment = Comentario(apodo,titulo,detalle,_id_contenido)  
        db.session.add(newComment)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))
    return render_template('nuevoComentario.html', id = _id_contenido)


#las replicas de las replicas se distinguen con id_comentairio=0
@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/replica",methods=['GET'])
def obtenerReplicas(_id_contenido, id_comentario):
    replicas= Replica.query.filter_by(id_comentario=id_comentario)
    com = Comentario.query.filter_by(id=id_comentario).first()
    return render_template('replicas.html',replicas=replicas, id_contenido=_id_contenido, comentario = com)


@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/replica/<int:id_replica>",methods=['GET'])
def obtenerReplicasDeReplicas(_id_contenido, id_comentario, id_replica):
    # replicas = db.session.execute(f"""SELECT t.apodo,t.descripcion,t.id_comentario,t.id
    #                 FROM replica as t , tiene as x
    #                 WHERE t.id = x.id_replica_siguiente AND x.id_replica_actual={_id_replica} """)
    replicas = Replica.query.filter_by(id=id_replica).first()
    return render_template('replicasDeReplicas.html', replicas=replicas.rel, id_comentario=id_comentario, id_contenido = _id_contenido, id=id_replica)


#genera replicas :)
def func():
    replica1 = Replica(apodo= f"Gonza", descripcion = ("Soy una replica de replica"), id_comentario=0)
    replica2 = Replica(apodo= f"Rodo", descripcion = ("Soy una replica de replica"), id_comentario=0)
    replica3= Replica(apodo= f"Juli", descripcion = ("Soy una replica de replica"), id_comentario=0)
    db.session.add(replica1)
    db.session.add(replica2)
    db.session.add(replica3)

    db.session.commit()