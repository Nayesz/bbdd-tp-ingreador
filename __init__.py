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

@app.route("/",methods=['GET'])
def home():
    return render_template("home.html")

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
    return render_template('editarComentario.html',comentario=_comentario, id = _comentario.id_contenido)

@app.route("/<int:id_contenido>/nuevoComentario",methods=['GET','POST'])
def comentario(id_contenido):
    if request.method == 'POST':
        apodo = request.form.get('apodo')
        titulo= request.form.get('titulo')
        detalle = request.form.get('detalle')
        newComment = Comentario(apodo,titulo,detalle,id_contenido)  
        db.session.add(newComment)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = id_contenido))
    return render_template('nuevoComentario.html',id_contenido=id_contenido, id = id_contenido)

@app.route("/<int:_id_contenido>/obtenerComentario",methods=['GET'])
def obtenerComentario(_id_contenido):
    comentarios= Comentario.query.filter_by(id_contenido=_id_contenido)
    print(comentarios)
    return render_template('mostrarComentarios.html',comentarios=comentarios, id = _id_contenido)

@app.route("/<int:_id_contenido>/obtenerComentario/<int:_id_comentario>/replicas",methods=['GET'])
def obtenerReplicas(_id_contenido, _id_comentario):
    replicas= Replica.query.filter_by(id_comentario=_id_comentario)
    # func(_id_comentario) 
    return render_template('replicas.html',replicas=replicas, id_contenido=_id_contenido)

@app.route("/<int:_id_contenido>/obtenerComentario/<int:_id_comentario>/replicas/<int:_id_replica>",methods=['GET'])
def obtenerReplicasDeReplicas(_id_contenido, _id_comentario, _id_replica):
    # replicas = db.session.execute(f"""SELECT t.apodo,t.descripcion,t.id_comentario,t.id
    #                 FROM replica as t , tiene as x
    #                 WHERE t.id = x.id_replica_siguiente AND x.id_replica_actual={_id_replica} """)
    replicas = Replica.query.filter_by(id=_id_replica).first()
    return render_template('replicasDeReplicas.html', replicas=replicas.rel, id_comentario=_id_comentario, id_contenido = _id_contenido)


#genera replicas :)
def func(_id_comentario):
    for i in range(10):
        replica = Replica(apodo= f"apo{i}", descripcion = ("a"*i), id_comentario=_id_comentario)
        db.session.add(replica)
        db.session.commit()