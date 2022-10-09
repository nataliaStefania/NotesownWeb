class Notas():

    def __init__(self,nombre_nota=None, descripcion_nota=None, fk_id_carpeta=None,fecha_creacion_nota=None,fecha_edicion_nota=None, ultimo_editor_nota=None,panel_nota=None, id_nota=None):

        self.name = nombre_nota        
        self.description = descripcion_nota
        self.parentFolder = fk_id_carpeta
        self.creationDate = fecha_creacion_nota
        self.updateDate = fecha_edicion_nota
        self.lastEditor = ultimo_editor_nota
        self.panel = panel_nota
        self.id = id_nota
        
    
    def to_JSON(self):
        return{
            'name': self.name,
            'description': self.description,
            'parentFolder': self.parentFolder,
            'creationDate': self.creationDate,
            'updateDate': self.updateDate,
            'lastEditor': self.lastEditor,
            'panel': self.panel,
            'id': self.id,
        }

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)