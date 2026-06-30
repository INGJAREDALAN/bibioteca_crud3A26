from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO: 

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""SELECT usuario.id, usuario.nombre, usuario.matricula, usuario.correo, carrera.carrera FROM usuario JOIN carrera ON usuario.carrera = carrera.id;""")
        registros  = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = Usuario(
            id=registro[0],
            nombre=registro[1],
            matricula=registro[2],
            correo=registro[3],
            carrera=registro[4]
            )
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios
    
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql= """
        INSERT INTO usuario (id, nombre, matricula, carrera, correo)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (usuario.id,
            usuario.nombre,
            usuario.matricula,
            usuario.correo,
            usuario.carrera
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET nombre = %s, matricula = %s, carrera = %s, 
        correo = %s
        WHERE id = %s
        """
        cursor.execute(
            sql,
            (usuario.nombre,
            usuario.matricula,
            usuario.correo,
            usuario.carrera,
            usuario.id)
        )

    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
                "DELETE FROM usuario WHERE id = %s",
                (id,)
                )
            
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]
