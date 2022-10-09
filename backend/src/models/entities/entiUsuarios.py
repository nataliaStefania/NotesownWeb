class Usuarios():

    def __init__(self,nombres_usuario=None, apellidos_usuario=None,correo_usuario=None,clave_usuario=None,imagen_usuario=None, id_usuario=None):
        self.name = nombres_usuario
        self.lastname = apellidos_usuario
        self.email = correo_usuario
        self.passw = clave_usuario
        self.img = imagen_usuario
        self.id = id_usuario
    
    def to_JSON(self):
        return{
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'passw': self.passw,
            'img': self.img,
            'id': self.id,
        }
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)