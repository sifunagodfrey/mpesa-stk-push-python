from flask import Flask, request, render_template, jsonify
from config import Config
import requests
import base64
from datetime import datetime

app = Flask(__name__)
config = Config()

def get_access_token():
    url = f"{config.base_url}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(config.consumer_key, config.consumer_secret))
    return response.json().get('access_token')

def lipa_na_mpesa_online(phone, amount):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((config.shortcode + config.passkey + timestamp).encode()).decode()
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": config.shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": config.shortcode,
        "PhoneNumber": phone,
        "CallBackURL": config.callback_url,
        "AccountReference": "Test123",
        "TransactionDesc": "Payment"
    }

    response = requests.post(f"{config.base_url}/mpesa/stkpush/v1/processrequest", headers=headers, json=payload)
    return response.json()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    phone = request.form['phone']
    amount = request.form['amount']
    response = lipa_na_mpesa_online(phone, amount)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)