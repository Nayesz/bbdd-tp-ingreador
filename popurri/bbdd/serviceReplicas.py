from replicaDAO import ReplicaDAO

class ServiceReplicas():

    @classmethod
    def traerReplicasDelComentario(cls, id_comentario):
        ReplicaDAO.select(id_comentario)
