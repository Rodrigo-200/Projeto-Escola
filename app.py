from flask import Flask, request
import requests
import json
import git

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    print("Received data:", data)
    json_url = 'https://indigo-guttural-daphne.glitch.me/webhook'

    # Fetch the current data
    response = requests.get(json_url)
    if response.status_code == 200:
        current_data = response.json()
        current_data.update(data)  # Assumes you want to update or add new entries

        # Update the data back to the server via API (method needs to be implemented on Glitch)
        update_response = requests.post(json_url, json=current_data)
        if update_response.status_code == 200:
            print("Data successfully updated on Glitch")
        else:
            print("Failed to update data on Glitch")
    else:
        print("Failed to fetch the current data")

    repo_dir = r'C:\Users\rodri\Downloads\Projeto-Escola'
    repo = git.Repo(repo_dir)
    repo.git.add('.')
    repo.index.commit("Update sensor data")
    origin = repo.remote(name='origin')
    origin.push()

    return 'Data updated', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
