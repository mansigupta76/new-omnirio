from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from dotenv import load_dotenv
from api_books import (
    get_loyalty_gift_received, get_loyalty_levels,
    create_customers_info, get_customer_details,
    update_customer_info, get_customers,
    get_customer_rewards, get_customer_transactions,
    get_transaction_types, create_transaction, 
    get_company_transactions
)


load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "App is running......"})
    

@app.route('/api/customers/create', methods=['POST'])
def create_customers():
    if request.method == 'POST':
        data = request.json
        result = create_customers_info(data)
        return result
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/customers/update', methods=['POST'])
def update_customers():
    if request.method == 'POST':
        data = request.json
        result = update_customer_info(data)
        return result
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})


@app.route('/api/customers/<customer_email_id>/details', methods=['GET'])
def customer_details(customer_email_id):
    if request.method == 'GET':
        print(customer_email_id)
        result = get_customer_details(customer_email_id)
        return result
    else:
        return jsonify({"message": "Send a GET request to this endpoint"})



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






# Get Customers (with pagination and filters)
@app.route('/api/customers', methods=['POST'])
def customers():
    if request.method == 'POST':
        data = request.json
        q = data.get("q")
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        sort_name = data.get("sort_name")
        sort_created_at = data.get("sort_created_at")
        filters = data.get("filters")
        result = get_customers(q, page_number, per_page, sort_name, sort_created_at, filters)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/customer_rewards', methods=['POST'])
def customer_rewards():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        phone = data.get("phone")
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        result = get_customer_rewards(email, phone, page_number, per_page)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/customer_transactions', methods=['POST'])
def customer_transactions():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        phone = data.get("phone")
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        result = get_customer_transactions(email, phone, page_number, per_page)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/loyalty_levels', methods=['POST'])
def loyalty_levels():
    if request.method == 'POST':
        data = request.json
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        result = get_loyalty_levels(page_number, per_page)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/loyalty_gift_received', methods=['POST'])
def loyalty_gift_received():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        phone = data.get("phone")
        gift_code = data.get("gift_code")
        result = get_loyalty_gift_received(email, phone, gift_code)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/transaction_types', methods=['POST'])
def transaction_types():
    if request.method == 'POST':
        data = request.json
        q = data.get("q")
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        result = get_transaction_types(q, page_number, per_page)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/transactions/create', methods=['POST'])
def create_transaction_view():
    if request.method == 'POST':
        data = request.json
        result = create_transaction(data)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})

@app.route('/api/company_transactions', methods=['POST'])
def company_transactions():
    if request.method == 'POST':
        data = request.json
        q = data.get("q")
        page_number = data.get("page_number", 1)
        per_page = data.get("per_page", 10)
        sort_total = data.get("sort_total")
        result = get_company_transactions(q, page_number, per_page, sort_total)
        return jsonify(result)
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})


if __name__ == '__main__':
    app.run(debug=True)
