from flask import Blueprint, request, jsonify
from models import Laptops
from laptop_crud import *

laptops_blueprint = Blueprint('laptops', __name__)

# In-memory storage for laptops
laptops = {}

# Add a Laptop
@laptops_blueprint.route('/laptops/add', methods=['POST'])
def add_laptop():
    data = request.get_json()
    name = data.get('name')
    laptop_number = data.get('laptop_number')
    specifications = data.get('specifications')

    if not name or not laptop_number or not specifications:
        return jsonify({"error": "Missing required fields"}), 400

    if laptop_number in laptops:
        return jsonify({"error": "Laptop number must be unique"}), 400

    laptops[laptop_number] = {
        "name": name,
        "specifications": specifications
    }
    return jsonify({"message": "Laptop added successfully"}), 201

# Get All Laptops
@laptops_blueprint.route('/laptops', methods=['GET'])
def get_all_laptops():
    return jsonify(laptops), 200

# Get a Laptop by Name
@laptops_blueprint.route('/laptops/name/<name>', methods=['GET'])
def get_laptop_by_name(name):
    for laptop in laptops.values():
        if laptop['name'] == name:
            return jsonify(laptop), 200
    return jsonify({"error": "Laptop not found"}), 404

# Get a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/number/<laptop_number>', methods=['GET'])
def get_laptop_by_number(laptop_number):
    laptop = laptops.get(laptop_number)
    if laptop:
        return jsonify(laptop), 200
    return jsonify({"error": "Laptop not found"}), 404

# Update a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/update/<laptop_number>', methods=['PUT'])
def update_laptop(laptop_number):
    data = request.get_json()
    laptop = laptops.get(laptop_number)

    if not laptop:
        return jsonify({"error": "Laptop not found"}), 404

    laptops[laptop_number].update(data)
    return jsonify({"message": "Laptop updated successfully"}), 200

# Delete a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/delete/<laptop_number>', methods=['DELETE'])
def delete_laptop(laptop_number):
    if laptop_number in laptops:
        del laptops[laptop_number]
        return jsonify({"message": "Laptop deleted successfully"}), 200
    return jsonify({"error": "Laptop not found"}), 404

#Make sure to register this blueprint in your main Flask application file:

from flask import Flask
from laptops_blueprint import laptops_blueprint

app = Flask(__name__)
app.register_blueprint(laptops_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
