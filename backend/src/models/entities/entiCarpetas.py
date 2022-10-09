class Carpetas():

    def __init__(self, nombre_carpeta=None, fecha_creacion_carpeta=None, fecha_edicion_carpeta=None, panel_carpeta=None, id_carpeta=None):
        self.name = nombre_carpeta        
        self.creationDate = fecha_creacion_carpeta
        self.updateDate = fecha_edicion_carpeta
        self.panel = panel_carpeta
        self.id = id_carpeta
        
    
    def to_JSON(self):
        return{
            'name': self.name,
            'creationDate': self.creationDate,
            'updateDate': self.updateDate,
            'panel': self.panel,
            'id': self.id,
        }
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)