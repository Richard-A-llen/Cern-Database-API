from flask import Flask, jsonify, request
import crud
from db_and_table import create_tables

app = Flask(__name__)


@app.route('/files', methods=["GET"])
def get_files():
    files = crud.get_files()
    return jsonify(files)

@app.route('/file', methods=["POST"])
def insert_file():
    file_details = request.get_json()
    name = file_details["name"]
    format = file_details["format"]
    size = file_details["size"]
    result = crud.insert_file(name, format,size)
    return jsonify(result)

@app.route('/file', methods=["PUT"])
def update_file():
    file_details = request.get_json()
    id = file_details["id"]
    name = file_details["name"]
    format = file_details["format"]
    size = file_details["size"]
    result = crud.update_file(id, name, format,size)
    return jsonify(result)

@app.route('/file/<id>', methods=["DELETE"])
def delete_file(id):
    result = crud.delete_file(id)
    return jsonify(result)

@app.route('/file/<id>', methods=["GET"])
def get_file_by_id(id):
    file = crud.get_file_by_id(id)
    return jsonify(file)


if __name__ == "__main__":
    create_tables()
    app.run()

