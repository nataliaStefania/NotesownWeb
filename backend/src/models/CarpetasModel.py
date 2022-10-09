from database.db import get_connection
from .entities.entiCarpetas import Carpetas
from .entities.entiNotas import Notas
from datetime import datetime

class CarpetasModel():
    #Buscar todos
    @classmethod
    def get_carpetas(self):
        try:
            connection=get_connection()
            carpetas=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre_carpeta, fecha_creacion_carpeta, fecha_edicion_carpeta, panel_carpeta, id_carpeta FROM carpetas ORDER BY id_carpeta")
                resultset=cursor.fetchall()

                for row in resultset:
                    carpeta  = Carpetas(row[0],row[1],row[2],row[3],row[4])
                    carpetas.append(carpeta.to_JSON())

            connection.close()
            return carpetas
        except Exception as ex:
            raise Exception(ex)

    #Buscar uno
    @classmethod
    def get_carpeta(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre_carpeta, fecha_creacion_carpeta, fecha_edicion_carpeta, panel_carpeta, id_carpeta FROM carpetas WHERE id_carpeta = %s",[id])
                row = cursor.fetchone()

                carpeta = None
                if row != None:
                        carpeta = Carpetas(row[0],row[1],row[2],row[3],row[4])
                        carpeta = carpeta.to_JSON()
                    
            connection.close()
            return carpeta
        except Exception as ex:
            raise Exception(ex)

    # Añadir 
    @classmethod
    def add_carpeta(self, carpeta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO carpetas (id_carpeta, nombre_carpeta, panel_carpeta) VALUES (DEFAULT, %s, %s) RETURNING id_carpeta", (carpeta.name, 0))
                response = [cursor.rowcount, cursor.fetchone()[0]]
                affected_rows  = cursor.rowcount
                connection.commit()
                
            connection.close()
            return response
        except Exception as ex:
            raise Exception(ex)

    #Asignar editor a la nota
    @classmethod
    def asignEditor(self, id_carpeta, id_editor, id_rol):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO usuarios_carpetas (fk_id_usuario, fk_id_carpeta, fk_id_rol) VALUES (%s, %s, %s)", [id_editor, id_carpeta, id_rol])
                affected_rows  = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

 # Actualizar
    @classmethod
    def update_carpeta(self, carpeta):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE carpetas SET nombre_carpeta = %s, fecha_edicion_carpeta = %s, panel_carpeta = %s WHERE id_carpeta = %s",(carpeta[0], datetime.now() , carpeta[1], carpeta[2]))
                
                affected_rows  = cursor.rowcount
                connection.commit()
      
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Eliminar
    @classmethod
    def delete_carpeta(self, id_owner, id_folder):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM carpetas WHERE id_carpeta = %s", [id])
                
                affected_rows  = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Traer carpetas por panel
    @classmethod
    def getFoldersByIdPanel(selft, id_owner, panel):
        try:
            connection=get_connection()
            carpetas=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre_carpeta, fecha_creacion_carpeta, fecha_edicion_carpeta, panel_carpeta, id_carpeta FROM carpetas INNER JOIN usuarios_carpetas ON id_carpeta = fk_id_carpeta INNER JOIN usuarios ON id_usuario = fk_id_usuario WHERE fk_id_usuario = %s AND panel_carpeta = %s",[id_owner, panel])
                resultset=cursor.fetchall()

                for row in resultset:
                    notas=[]
                    cursor.execute("SELECT  nombre_nota, descripcion_nota, fk_id_carpeta,  fecha_creacion_nota, fecha_edicion_nota,  ultimo_editor_nota, panel_nota ,id_nota FROM notas WHERE fk_id_carpeta = %s",[row[4]])
                    resultsetNotes=cursor.fetchall()
                    print(row[4])
                    for rowNote in resultsetNotes:
                        nota  = Notas(rowNote[0],rowNote[1],rowNote[2],rowNote[3],rowNote[4],rowNote[5],rowNote[6],rowNote[7])
                        notas.append(nota.to_JSON())
                    
                    carpeta  = Carpetas(row[0],row[1],row[2],row[3],row[4])
                    carpetas.append({"folder": carpeta.to_JSON(), "notes": notas})

            connection.close()
            return carpetas
        except Exception as ex:
            raise Exception(ex)
