from comentarioDAO import ComentarioDAO

class ServiceComentarios():

    @classmethod
    def traerComentariosDelContenido(cls, id_contenido):
        ComentarioDAO.select(id_contenido)

    @classmethod
    def traerComentario(cls, id_comentario):
        ComentarioDAO.selectComentario(id_comentario)



if __name__ == "__main__":
    print(len(ServiceComentarios.traerComentariosDelContenido(3)))