from conexion import Conexion
from comentario import Comentario

class ComentarioDAO():
    _INSERT = """INSERT INTO comentario(titulo, descripcion, apodo_comentarista, id_contenido)
                     VALUES(%s, %s, %s, %s)"""
    _SELECT_BY_CONTENIDO = "SELECT * FROM comentario WHERE id_contenido=%s ORDER BY id_comentario"
    _SELECT_COMENTARIO = "SELECT * FROM comentario WHERE id_comentario=%s"
    _UPDATE = """UPDATE comentario SET titulo=%s, descripcion=%s, apodo_comentarista=%s, id_contenido=%s 
                    WHERE id_comentario = %s"""
    _DELETE = "DELETE FROM comentario WHERE id_comentario=%s"

    @classmethod
    def insert(cls, comentario):
        cursor = Conexion.obtenerCursor()
        valores = (comentario.titulo, comentario.descripcion, comentario.apodo, 
                        comentario.id_contenido)
        cursor.execute(cls._INSERT, valores)
        Conexion.cerrar()

    @classmethod
    def select(cls, id_contenido):
        cursor = Conexion.obtenerCursor()
        comentarios = []
        valor = (id_contenido,)
        cursor.execute(cls._SELECT_BY_CONTENIDO, valor)
        respuesta = cursor.fetchall()
        for resp in respuesta:
            comentario = Comentario(id=resp[0], titulo=resp[1], descripcion=resp[2], apodo=resp[3], id_contenido=resp[4])
            comentarios.append(comentario)
        Conexion.cerrar()
        return comentarios

    @classmethod
    def selectComentario(cls, id_comentario):
        cursor = Conexion.obtenerCursor()
        valor = (id_comentario,)
        cursor.execute(cls._SELECT_COMENTARIO, valor)
        resp = cursor.fetchone()
        comentario = Comentario(id=resp[0], titulo=resp[1], descripcion=resp[2], apodo=resp[3], id_contenido=resp[4])
        Conexion.cerrar()
        return comentario

    @classmethod
    def delete(cls, id_comentario):
        cursor = Conexion.obtenerCursor()
        valor = (id_comentario,)
        cursor.execute(cls._DELETE, valor)
        Conexion.cerrar()

    @classmethod
    def update(cls, comentario):
        cursor = Conexion.obtenerCursor()
        valores = (comentario.titulo, comentario.descripcion, comentario.apodo, 
                        comentario.id_contenido, comentario.id)
        cursor.execute(cls._UPDATE, valores)
        Conexion.cerrar()

if __name__ == "__main__":
    # comentarioEj = Comentario(titulo="titulo original", descripcion="descripcion descriptiva", apodo="gperezzzzz", id_contenido=3)
    # comentarioEjconID = Comentario(titulo="titulo no original", descripcion="descripcion no descriptiva", apodo="gperezzzzz", id_contenido=3, id= 306)
    # ComentarioDAO.insert(comentarioEj)
    # print(len(ComentarioDAO.select(3)))
    print(ComentarioDAO.selectComentario(261))
    # ComentarioDAO.delete(305)
    # ComentarioDAO.update(comentarioEjconID)