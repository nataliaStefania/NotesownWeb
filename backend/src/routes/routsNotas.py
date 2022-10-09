from flask import Blueprint, jsonify, request

# Entities
from models.entities.entiNotas import Notas
# Models
from models.NotasModel import NotasModel

main = Blueprint('nota_blueprint',  __name__)

#Buscar todos
@main.route('/') 
def get_notas():
    try:
        notas = NotasModel.get_notas()
        return jsonify(notas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

#Buscar uno
@main.route('/<id>')
def get_nota(id):
    try:
        nota = NotasModel.get_nota(id)
        if nota != None:
            return jsonify(nota)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

# Añadir 
@main.route('/add', methods = ['POST'])
def add_nota():
    try:
        name = request.json['name']
        description = request.json['description']
        parentFolder = request.json['parentFolder']
        lastEditor = request.json['lastEditor']

        nota = [name, parentFolder, description, lastEditor]
        affected_rows = NotasModel.add_nota(nota)

        if affected_rows == 1:
            return jsonify('message' f'Nota "{name}" creada.')
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500 

# Actualizar
@main.route('/update/<id>', methods = ['PUT'])
def update_nota(id):
    try:
        
        name = request.json['name']
        parentFolder = request.json['parentFolder']
        description = request.json['description']
        lastEditor = request.json['lastEditor']
        panel = request.json['panel']


        nota =[name, parentFolder, description, lastEditor, panel, id]

        affected_rows = NotasModel.update_nota(nota)

        if affected_rows == 1:
            return jsonify(f'Nota con ID {id} actualizada satisfactoriamente.')
        else:
            return jsonify({'message': "No note updated"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 

#Eliminar
@main.route('/delete/<id>', methods = ['DELETE'])
def delete_nota(id):
    try:
        affected_rows = NotasModel.delete_nota(id)

        if affected_rows == 1:
            return jsonify( f'Nota con ID {id} borrada satisfactoriamente.')
        else:
            return jsonify({'message': "No folder delete"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 