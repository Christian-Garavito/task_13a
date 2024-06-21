from flask import Flask, jsonify,request
from database import *


application = Flask(__name__)

@application.route("/")
def hello_world():

    return "<p>Hello, World kalsjlkasdjlasd!</p>"

# obtener todo el contenido
@application.route('/contenidos', methods=['GET'])
def get_contenido():

    result = read_contenidos()

    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "No data found"}), 404 # cuando no encuntra la pagina


 # agregar un contenido
@application.route('/contenidos', methods=['POST'])
def post_contenido():
    data = request.json
    create_contenido(data.get('pk_id_peliculas'), data.get('titulo_pelicula'), data.get('ano_pelicula'), data.get('fk_id_tipo_contenido'), data.get('director_pelicula'),data.get('valor_pelicula'))
    return jsonify({"message": "crear contenido"}), 201

 # editar un contenido
@application.route('/contenidos/<pk_id_peliculas>', methods=['PUT'])
def put_comando(pk_id_peliculas):
    data = request.json
    update_comando(pk_id_peliculas, data.get('titulo_pelicula'), data.get('ano_pelicula'), data.get('fk_id_tipo_contenido'), data.get('director_pelicula'), data.get('valor_pelicula'))
    return jsonify({"message": "contenido editado"}), 200

if __name__ == "__main__":
    application.run(debug=True)