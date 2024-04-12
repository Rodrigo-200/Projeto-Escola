from flask import Flask, request
import json
import git

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    print("Received data:", data)

    json_file_path = 'C:\\Users\\rodri\\Downloads\\Projeto-Escola\\data.json'

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    repo_dir = r'C:\Users\rodri\Downloads\Projeto-Escola'
    repo = git.Repo(repo_dir)
    repo.git.add('data.json')
    repo.index.commit("Update sensor data")
    origin = repo.remote(name='origin')
    origin.push()


    return 'Data updated', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
