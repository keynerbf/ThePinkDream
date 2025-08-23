import psycopg2

def conectar():
    try:
        conexion=psycopg2.connect(
            user="postgres",
            password="keyner123",
            host="localhost",
            port="5432",
            database="usuarios"
        )
        print("Conexión exitosa")
        return conexion
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a PostgreSQL:", error)
        return None

def desconectar(conexion):
    if conexion is not None:
        conexion.close()
        print("Conexión a PostgreSQL cerrada")