from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({"message": "To-Do app chal raha hai"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({"message": "Task added", "tasks": tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
