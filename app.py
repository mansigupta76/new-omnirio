from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from dotenv import load_dotenv
from api_books import get_customer_rewards,get_loyalty_levels,get_loyalty_gift_received

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "App is running......"})
    

@app.route('/api/customer_rewards', methods=['POST'])
def customer_rewards():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        result = get_customer_rewards(email)
        return result
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})


@app.route('/api/loyality_gift_received', methods=['POST'])
def loyality_gift_received():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        result = get_loyalty_gift_received(email)
        return result
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})



@app.route('/api/loyality_levels', methods=['POST'])
def loyality_levels():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        result = get_loyalty_levels(email)
        return result
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

if __name__ == '__main__':
    app.run(debug=True)
