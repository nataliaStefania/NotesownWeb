from database.db import get_connection
from .entities.entiUsuarios import Usuarios

class UsuariosModel():
    #Buscar todos
    @classmethod
    def get_usuarios(self):
        try:
            connection=get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT nombres_usuario, apellidos_usuario, correo_usuario, clave_usuario, imagen_usuario, id_usuario FROM usuarios ")
                resultset=cursor.fetchall()

                for row in resultset:
                    usuario = Usuarios(row[0],row[1],row[2],row[3],row[4],row[5])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
    #Buscar uno
    @classmethod
    def get_usuario(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombres_usuario, apellidos_usuario, correo_usuario, clave_usuario, imagen_usuario FROM usuarios WHERE id_usuario = %s",(id,))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                        usuario = Usuarios(row[0],row[1],row[2],row[3],row[4], row[5])
                        usuario = usuario.to_JSON()
                    
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)
    # Añadir 
    @classmethod
    def add_usuario(self,usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (nombres_usuario, apellidos_usuario, correo_usuario, clave_usuario, imagen_usuario) VALUES (%s, %s, %s, %s, %s )""",(usuario.name, usuario.lastname, usuario.email, usuario.passw, usuario.img))
                
                affected_rows  = cursor.rowcount
                connection.commit()
                
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    # Actualizar
    @classmethod
    def update_usuario(self,usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE usuarios SET nombres_usuario = %s, apellidos_usuario = %s, correo_usuario = %s, clave_usuario = %s WHERE id_usuario = %s",(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                
                affected_rows  = cursor.rowcount
                connection.commit()
      
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Eliminar
    @classmethod
    def delete_usuario(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", [id])
                
                affected_rows  = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)