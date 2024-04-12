from flask import Flask, request, jsonify
import json
import git
from threading import Timer

app = Flask(__name__)

# Path to the JSON file
json_file_path = 'C:\\Users\\rodri\\Downloads\\Projeto-Escola\\data.json'

# Default data to write when the timeout occurs
default_data = {
    "temperaturwa_ar": "A carregar...",
    "humidadwe_ar": "A carregar...",
    "humidadwe_solo": "A carregar...",
    "necessidadwe_rega": "A carregar...",
    "estado2_conexao": "Desconectado"
}

# Timer setup
timeout_duration = 70  # 70 seconds
timeout_timer = None

def update_json_on_timeout():
    with open(json_file_path, 'w') as json_file:
        json.dump(default_data, json_file, indent=4)
    commit_and_push_changes("Updated due to timeout")

def reset_timeout_timer():
    global timeout_timer
    if timeout_timer:
        timeout_timer.cancel()
    timeout_timer = Timer(timeout_duration, update_json_on_timeout)
    timeout_timer.start()

def commit_and_push_changes(message):
    repo_dir = r'C:\Users\rodri\Downloads\Projeto-Escola'
    repo = git.Repo(repo_dir)
    repo.git.add('data.json')
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()

@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    print("Received data:", data)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    commit_and_push_changes("Update sensor data")
    reset_timeout_timer()

    return jsonify({"message": "Data updated"}), 200

if __name__ == '__main__':
    reset_timeout_timer()  # Initialize the timer when the server starts
    app.run(debug=True, host='192.168.1.89', port=5000)
