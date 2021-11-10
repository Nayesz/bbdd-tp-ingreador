import mysql.connector as bd

class Conexion:
    _DATABASE = 'contentappdb'
    _USERNAME = 'root'
    _PASSWORD = 'root'
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                print("Conexion exitosa")
                return cls._conexion
            except Exception as e:
                print(f"Error: {e}")
                # sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print("Se abrió correctamente el cursor")
                return cls._cursor
            except Exception as e:
                print(f"Error: {e}")
                # sys.exit()
        else:
            return cls._cursor

    @classmethod
    def cerrar(cls):
        cls._conexion.commit()
        cls._cursor.close()
        cls._conexion.close()


if __name__ == "__main__":
    Conexion.obtenerCursor()
    print("Chau")