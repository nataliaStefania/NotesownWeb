from os import access
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_cors import cross_origin
from utils.token import writeToken
# Entities
from models.entities.entiUsuarios import Usuarios
# Models
from models.UsuariosModel import UsuariosModel

main = Blueprint('usuario_blueprint',  __name__)

#Login
@cross_origin
@main.route('/login', methods = ['POST'])
def login():
    try:
        password = request.json['password']
        email = request.json['email']

        user = UsuariosModel.login(email)
        if user != None:
            passIsCorrect = check_password_hash(user["passw"], password)
            if passIsCorrect:
                refresh = create_refresh_token(identity=user["id"])
                access = create_refresh_token(identity=user["id"])
                #token = writeToken(data=user["id"])
                return jsonify({
                    "status": "ok",

                    "user": {
                        "refresh": refresh,
                        "acces": access,
                        "email": user["email"],
                        "name": user["name"],
                        "lastname": user["lastname"],
                        "img": user["img"]
                    },

                    "response": access
                    }),200
            else:
                return jsonify({"status": "fail", "response": "Credenciales inválidas"}),401
        else:
            return jsonify({"status": "fail", "response": "Usuario inválido"}),401
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar todos
@main.route('/') 
def get_usuarios():
    try:
        usuarios = UsuariosModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar usuario por ID
@main.route('getUserByID/<id>')
def get_usuario(id):
    try:
        usuario = UsuariosModel.get_usuario(id)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar usuario por Email
@main.route('getUserByEmail/<email>')
def getUserByEmail(email):
    try:
        usuario = UsuariosModel.getUserByEmail(email)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
 
# Añadir 
@main.route('/add', methods = ['POST'])
def add_usuario():
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        email = request.json['email']
        password = request.json['password']
        img = request.json['img']

        if len(password) < 8:
            return jsonify({'error': "La contraseña debe contener mínimo 8 caracteres."})
        
        pwd_hash = generate_password_hash(password)
        usuario = Usuarios(name,lastname,email,pwd_hash,img)

        affected_rows = UsuariosModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify({'message' f'Usuario {name} creado.'}), 200
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

# Actualizar
@main.route('/update/<id>', methods = ['PUT'])
def update_usuario(id):
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        email = request.json['email']
        passw = request.json['passw']
        
        usuario = [name, lastname, email, passw, id]

        affected_rows = UsuariosModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify('message' f' Usuario "{name}" actualizado.')
        else:
            return jsonify({'message': "No user updated"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

#Eliminar
@main.route('/delete/<id>', methods = ['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuarios(id)

        affected_rows = UsuariosModel.delete_usuario(id)

        if affected_rows == 1:
            return jsonify('message' f'Usuario con "{id}" eliminado.')
        else:
            return jsonify({'message': "No user delete"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 