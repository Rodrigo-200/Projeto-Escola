from flask import Flask, request
import git
import os

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_website():
    data = request.json
    # Process the data and update files as necessary

    # Assuming your current directory is a git repository
    repo_dir = '/path/to/your/repo'  # replace with the path to your repo
    repo = git.Repo(repo_dir)
    repo.git.add(A=True)
    repo.index.commit("Update from ESP8266")
    origin = repo.remote(name='origin')
    origin.push()

    return 'Update Successful', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
