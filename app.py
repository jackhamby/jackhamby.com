

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

server_data = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/cheese/<key>', methods=['PUT'])
def set_data(key):
    try:
        data = request.get_json()
        server_data[key] = data["value"]
    except Exception as e:
        return {'error' : str(e)}
    return {
        'success' : f'set {key} to value {data["value"]}'
    }

@app.route('/cheese/<key>', methods=['GET'])
def get_data(key):
    response = {}
    response[key] = server_data[key]
    return response

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=8000)