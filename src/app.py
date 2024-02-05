from flask import Flask, jsonify, request
# Nombre de la aplicación pora Flask
app = Flask(__name__)

# Tareas
todos = [
    { "label": "Primera tarea", "done": False },
    { "label": "Segundo tarea", "done": False }
]

# Ruta para recibir el contenido
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Ruta para añadir tareas
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

# Ruta para eliminar tareas
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)
# Definir el puerto y el host
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)