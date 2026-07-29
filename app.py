from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Flask API! version 2222.0"})


@app.route("/employees")
def get_employees():
    return jsonify([{"id": 1, "name": "John"}, {"id": 2, "name": "Mary"}])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
