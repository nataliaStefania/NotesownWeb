from database.db import get_connection
from .entities.entiCarpetas import Carpetas
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
            print("Insertadas: " + carpeta.name)
            print(carpeta.panel)
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO carpetas (nombre_carpeta, panel_carpeta) VALUES (%s, %s)", (carpeta.name, 0))
                
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
    def delete_carpeta(self, id):
        try:
            connection = get_connection()
            print(id)
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM carpetas WHERE id_carpeta = %s", [id])
                
                affected_rows  = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)