from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data.json')
def data_json():
    return send_from_directory('.', 'data.json')

if __name__ == '__main__':
    app.run(port=8000)
