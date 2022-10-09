from database.db import get_connection
from .entities.entiNotas import Notas
from datetime import datetime

class NotasModel():
    #Buscar todos
    @classmethod
    def get_notas(self):
        try:
            connection=get_connection()
            notas=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT  nombre_nota, descripcion_nota, fk_id_carpeta,  fecha_creacion_nota, fecha_edicion_nota,  ultimo_editor_nota, panel_nota ,id_nota FROM notas ORDER BY id_nota")
                resultset=cursor.fetchall()

                for row in resultset:
                    nota = Notas(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    notas.append(nota.to_JSON())

            connection.close()
            return notas
        except Exception as ex:
            raise Exception(ex)
    
     #Buscar uno
    @classmethod
    def get_nota(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre_nota, descripcion_nota, fk_id_carpeta, fecha_creacion_nota, fecha_edicion_nota,  ultimo_editor_nota, panel_nota, id_nota FROM notas WHERE id_nota = %s",(id))
                row = cursor.fetchone()

                nota = None
                if row != None:
                        nota = Notas(row[0],row[1],row[2],row[3],row[4], row[5],row[6],row[7])
                        nota = nota.to_JSON()
                    
            connection.close()
            return nota
        except Exception as ex:
            raise Exception(ex)

    # Añadir 
    @classmethod
    def add_nota(self, nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO notas (nombre_nota, fk_id_carpeta, descripcion_nota, ultimo_editor_nota) VALUES (%s, %s, %s, %s)", (nota[0], nota[1], nota[2], nota[3]))
                
                affected_rows  = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
     # Actualizar
    @classmethod
    def update_nota(self,nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE notas SET nombre_nota = %s, fk_id_carpeta = %s, fecha_edicion_nota = %s, descripcion_nota = %s, ultimo_editor_nota = %s ,  panel_nota = %s WHERE id_nota = %s", (nota[0], nota[1], datetime.now() ,  nota[2],  nota[3], nota[4], nota[5]))
                
                affected_rows  = cursor.rowcount
                connection.commit()
      
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    #Eliminar
    @classmethod
    def delete_nota(self, id):
        try:
            connection = get_connection()
            print(id)
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM notas WHERE id_nota = %s", [id])
                
                affected_rows  = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)