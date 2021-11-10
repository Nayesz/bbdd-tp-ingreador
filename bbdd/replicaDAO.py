from conexion import Conexion
from replica import Replica

class ReplicaDAO():
    _INSERT = "INSERT INTO replica(detalle, apodo_replica, id_comentario) VALUES(%s, %s, %s)"
    _SELECT_BY_COMENTARIO = "SELECT * FROM replica WHERE id_comentario=%s ORDER BY id_replica"
    _SELECT_REPLICA = "SELECT * FROM replica WHERE id_replica=%s"
    _UPDATE = "UPDATE replica SET detalle=%s, apodo_replica=%s, id_comentario=%s WHERE id_replica=%s"
    _DELETE = "DELETE FROM replica WHERE id_replica=%s"

    @classmethod
    def insert(cls, replica):
        cursor = Conexion.obtenerCursor()
        valores = (replica.detalle, replica.apodo, replica.id_comentario)
        cursor.execute(cls._INSERT, valores)
        Conexion.cerrar()

    @classmethod
    def select(cls, id_comentario):
        cursor = Conexion.obtenerCursor()
        replicas = []
        valor = (id_comentario,)
        cursor.execute(cls._SELECT_BY_COMENTARIO, valor)
        respuesta = cursor.fetchall()
        for resp in respuesta:
            replica = Replica(id=resp[0], detalle=resp[1], apodo=resp[2], id_comentario=resp[3])
            replicas.append(replica)
        Conexion.cerrar()
        return replicas

    @classmethod
    def selectReplica(cls, id_replica):
        cursor = Conexion.obtenerCursor()
        valor = (id_replica,)
        cursor.execute(cls._SELECT_REPLICA, valor)
        resp = cursor.fetchone()
        replica = Replica(id=resp[0], detalle=resp[1], apodo=resp[2], id_comentario=resp[3])
        Conexion.cerrar()
        return replica

    @classmethod
    def delete(cls, id_replica):
        cursor = Conexion.obtenerCursor()
        valor = (id_replica,)
        cursor.execute(cls._DELETE, valor)
        Conexion.cerrar()

    @classmethod
    def update(cls, replica):
        cursor = Conexion.obtenerCursor()
        valores = (replica.detalle, replica.apodo, replica.id_comentario, replica.id)
        cursor.execute(cls._UPDATE, valores)
        Conexion.cerrar()

if __name__ == "__main__":
    # print(len(ReplicaDAO.select(18)))
    replEj= Replica("comentario infiltrado", "gonzzzzz", 18, id=301)
    ReplicaDAO.insert(replEj)
    # ReplicaDAO.update(replEj)
    # ReplicaDAO.delete(301)