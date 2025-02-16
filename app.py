from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_STORAGE = {}

@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task parameter is required"}), 400

    # Simulate processing
    response_data = {"task": task, "result": f"Processed: {task}"}
    file_path = f"{task}.json"

    # Store result
    DATA_STORAGE[file_path] = response_data
    return jsonify(response_data)

@app.route('/read', methods=['GET'])
def read_file():
    path = request.args.get('path')
    if not path or path not in DATA_STORAGE:
        return jsonify({"error": "File not found"}), 404

    return jsonify(DATA_STORAGE[path])

if __name__ == '__main__':
    app.run(debug=True)
