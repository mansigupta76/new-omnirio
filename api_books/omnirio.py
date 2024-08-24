import os
import requests
import json

def create_customers_info(data):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = base_url +"/api/client/v1/customers/create_customer"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = json.dumps(data)
    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def get_customer_details(customer_email):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = base_url + "/api/client/v1/customers/details"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = json.dumps({
        "email": customer_email
    })
    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    

    return response.json()







def update_customer_info(data):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/customers/update_customer"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = json.dumps(data)
    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response.json()



def get_customers(q=None, page_number=1, per_page=10, sort_name=None, sort_created_at=None, filters=None):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/customers/get_customers"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }
    if q:
        payload["q"] = q
    if sort_name or sort_created_at:
        payload["sort"] = {}
        if sort_name:
            payload["sort"]["name"] = sort_name
        if sort_created_at:
            payload["sort"]["created_at"] = sort_created_at
    if filters:
        payload["filters"] = filters

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_customer_rewards(customer_email=None, customer_phone=None, page_number=1, per_page=10):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/customers/get_customer_rewards"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }
    if customer_email:
        payload["email"] = customer_email
    if customer_phone:
        payload["phone"] = customer_phone

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_customer_transactions(customer_email=None, customer_phone=None, page_number=1, per_page=10):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/customers/transactions"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }
    if customer_email:
        payload["email"] = customer_email
    if customer_phone:
        payload["phone"] = customer_phone

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_loyalty_levels(page_number=1, per_page=10):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/loyalty_settings/get_loyalty_levels"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_loyalty_gift_received(customer_email=None, customer_phone=None, gift_code=None):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/customers/gift_received"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {}
    if customer_email:
        payload["email"] = customer_email
    if customer_phone:
        payload["phone"] = customer_phone
    if gift_code:
        payload["gift_code"] = gift_code

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_transaction_types(q=None, page_number=1, per_page=10):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/transactions/get_transaction_types"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }
    if q:
        payload["q"] = q

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def create_transaction(data):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/transactions/create_trasaction"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = json.dumps(data)
    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def get_company_transactions(q=None, page_number=1, per_page=10, sort_total=None):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = f"{base_url}/api/client/v1/transactions/get_transactions"
    auth_token = os.environ.get("AUTH_TOKEN")

    payload = {
        "page": {
            "number": page_number,
            "per_page": per_page
        }
    }
    if q:
        payload["q"] = q
    if sort_total:
        payload["sort"] = {"total": sort_total}

    headers = {
        'api-token': auth_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

