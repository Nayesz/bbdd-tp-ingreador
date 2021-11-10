from flask import Flask, render_template
from comentarioDAO import ComentarioDAO
from replicaDAO import ReplicaDAO
from serviceComentarios import ServiceComentarios
from serviceReplicas import ServiceReplicas

app = Flask(__name__)
# harcodeado el id del contenido
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/contenido/<int:id_contenido>/comentarios/')
def comentarios(id_contenido):
    comentarios = ComentarioDAO.select(id_contenido)
    return render_template('comentarios.html', coms = comentarios)

@app.route('/contenido/<int:id_contenido>/comentarios/<int:id_comentario>/')
def editarComentario(id_contenido, id_comentario):
    comentario = ComentarioDAO.selectComentario(id_comentario)
    return render_template('editarComentario.html', com = comentario)

@app.route('/contenido/<int:id_contenido>/comentarios/<int:id_comentario>/replicas')
def replicas(id_contenido, id_comentario):
    replicas = ReplicaDAO.select(id_comentario)
    return render_template('replicas.html', repl = replicas)

if __name__ == "__main__":
    app.run(debug=True)
