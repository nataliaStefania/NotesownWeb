class Usuarios():

    def __init__(self,id_usuario,nombre_usuario,apellidos_usuario,correo_usuario,clave_usuario,imagen_usuario) -> None:
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.apellidos_usuario = apellidos_usuario
        self.correo_usuario = correo_usuario
        self.clave_usuario = clave_usuario
        self.imagen_usuario = imagen_usuario
    
    def to_JSON(self):
        return{
            'id': self.id_usuario,
            'nombre_usuario': self.nombre_usuario,
            'apellidos_usuario': self.apellidos_usuario,
            'correo_usuario': self.correo_usuario,
            'clave_usuario': self.clave_usuario,
            'imagen_usuario': self.imagen_usuario,
        }

