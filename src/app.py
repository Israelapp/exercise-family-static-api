"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Initialize the Jackson family object
jackson_family = FamilyStructure("Jackson")


# --- ERROR HANDLING ---

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(500)
def handle_internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


# --- API ENDPOINTS ---

@app.route('/')
def sitemap():
    return generate_sitemap(app)


# 1. GET: Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_family_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 2. GET: Obtener un solo miembro por su ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    try:
        member = jackson_family.get_member(member_id)

        # Si el miembro no existe
        if not member:
            return jsonify({"error": f"Member with id {member_id} not found"}), 404

        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 3. POST: Crear/Añadir un nuevo miembro
@app.route('/member', methods=['POST'])
def add_new_member():
    try:
        # Obtenemos los datos enviados en el cuerpo (body) de la petición JSON
        body = request.get_json()

        # Validaciones básicas de campos obligatorios
        if not body:
            return jsonify({"error": "Body cannot be empty"}), 400
        if "first_name" not in body:
            return jsonify({"error": "first_name is required"}), 400
        if "age" not in body:
            return jsonify({"error": "age is required"}), 400
        if "lucky_numbers" not in body:
            return jsonify({"error": "lucky_numbers is required"}), 400

        # Si el cliente no envía un 'id', la estructura de datos debería generarlo automáticamente
        new_member = {
            "id": body.get("id"),  # Puede ser None y que la clase se encargue
            "first_name": body["first_name"],
            # Usamos el apellido de la familia por defecto
            "last_name": jackson_family.last_name,
            "age": body["age"],
            "lucky_numbers": body["lucky_numbers"]
        }

        # Añadimos el miembro usando el método de tu estructura
        jackson_family.add_member(new_member)

        return jsonify({"msg": "Member added successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 4. DELETE: Eliminar un miembro por su ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    try:
        # Intentamos obtener el miembro primero para verificar si existe
        member = jackson_family.get_member(member_id)
        if not member:
            return jsonify({"error": f"Member with id {member_id} not found"}), 404

        # Si existe, lo eliminamos
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- SERVER LAUNCH ---

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
