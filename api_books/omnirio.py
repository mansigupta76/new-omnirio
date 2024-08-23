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

def get_customer_rewards(customer_email):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = base_url + "/api/client/v1/customers/get_customer_rewards"
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





def get_loyalty_levels(customer_email):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = base_url + "/api/client/v1/loyalty_settings/get_loyalty_levels"
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


def get_loyalty_gift_received(customer_email):
    base_url = os.environ.get("OMNIRIO_BASE_URL")
    url = base_url + "/api/client/v1/customers/gift_received"
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