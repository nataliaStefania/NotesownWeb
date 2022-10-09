from flask import Blueprint, jsonify

# Models
from models.UsuariosModel import UsuariosModel

main=Blueprint('usuario_blueprint',  __name__)


@main.route('/') 
def get_usuarios():
    try:
        usuarios = UsuariosModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
