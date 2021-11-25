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
    return render_template("home.html")


@app.route("/contenido/<int:_id_contenido>/comentario/",methods=['GET'])
def obtenerComentario(_id_contenido):
    comentarios = db.session.execute(f"""SELECT * FROM comentario WHERE comentario.id_contenido={_id_contenido} """)
    # comentarios= Comentario.query.filter_by(id_contenido=_id_contenido)
    return render_template('mostrarComentarios.html',comentarios=comentarios, id = _id_contenido)


@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/delete",methods=['GET','DELETE'])
def borrarComentario(_id_contenido, id_comentario):
    db.session.execute(f"""DELETE FROM comentario WHERE comentario.id={id_comentario} """)
    # comentario= Comentario.query.filter_by(id=id_comentario).first()
    # db.session.delete(comentario)
    db.session.commit()
    return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))

@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/update",methods=['GET','POST'])
def editarComentario(_id_contenido, id_comentario):
    _comentario= db.session.execute(f"""SELECT * FROM comentario WHERE comentario.id={id_comentario} """).fetchone()
    print("el comentario:")
    # print(_comentario.fetchone())
    # _comentario= Comentario.query.filter_by(id=id_comentario).first()
    if request.method == 'POST':
        db.session.execute(f"""UPDATE comentario SET titulo="{request.form.get('titulo')}",descripcion="{request.form.get('descripcion')}" 
        WHERE comentario.id={id_comentario} """)
        # db.session.add(_comentario)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))
    return render_template('editarComentario.html', comentario=_comentario)


@app.route("/contenido/<int:_id_contenido>/comentario/create",methods=['GET','POST'])
def crearComentario(_id_contenido):
    if request.method == 'POST':
        db.session.execute(f"""INSERT INTO comentario (titulo,descripcion,apodo,id_contenido)
         VALUES ("{request.form.get('titulo')}","{request.form.get('descripcion')}","{request.form.get('apodo')}"
         ,"{_id_contenido}")""")
        # db.session.add(newComment)
        db.session.commit()
        return redirect(url_for('obtenerComentario', _id_contenido = _id_contenido))
    return render_template('nuevoComentario.html', id = _id_contenido)


#las replicas de las replicas se distinguen con id_comentairio=0
@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/replica",methods=['GET'])
def obtenerReplicas(_id_contenido, id_comentario):
    replicas = db.session.execute(f"""SELECT * FROM replica WHERE replica.id_comentario={id_comentario} """)
    # replicas= Replica.query.filter_by(id_comentario=id_comentario)
    com = db.session.execute(f"""SELECT * FROM comentario WHERE comentario.id={id_comentario} """).fetchone()
    # com = Comentario.query.filter_by(id=id_comentario).first()
    return render_template('replicas.html',replicas=replicas, id_contenido=_id_contenido, comentario = com)

@app.route("/contenido/<int:_id_contenido>/comentario/<int:id_comentario>/replica/<int:id_replica>",methods=['GET'])
def obtenerReplicasDeReplicas(_id_contenido, id_comentario, id_replica):
    replicas = db.session.execute(f"""SELECT t.apodo,t.descripcion,t.id_comentario,t.id
                    FROM replica as t , tiene as x
                    WHERE t.id = x.id_replica_siguiente AND x.id_replica_actual={id_replica} """)
    #replicas = Replica.query.filter_by(id=id_replica).first()
    return render_template('replicasDeReplicas.html', replicas=replicas, id_comentario=id_comentario, id_contenido = _id_contenido, id=id_replica)


#genera replicas :-)
def func():
    for i in range(10):
        replica = Replica(apodo= f"apo{i}", descripcion = ("a"*i), id_comentario=0)
        db.session.add(replica)
        db.session.commit()