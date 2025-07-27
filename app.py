from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import get_db
from chatboard_logic import generate_response
from model import format_log

app = Flask(__name__)
CORS(app)
db = get_db()
logs_col = db["logs"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get("query", "")
    response = generate_response(query)
    log = format_log(query, response)
    logs_col.insert_one(log)
    return jsonify({"response": response})

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(logs_col.find({}, {"_id": 0}))
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
