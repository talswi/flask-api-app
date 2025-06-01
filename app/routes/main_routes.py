from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

@main_routes.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "alive"})

