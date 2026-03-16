
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Cybersecurity Lab Dashboard"

@app.route("/stats")
def stats():
    data = {
        "alerts": random.randint(1,10),
        "attacks": random.randint(5,50),
        "vulnerabilities": random.randint(1,20)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
