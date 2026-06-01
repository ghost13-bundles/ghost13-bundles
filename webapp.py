from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "M-PESA Daraja API - Ghost 13 Bundles is live 🚀"

@app.route('/stkpush', methods=['POST'])
def stk_push():
    data = request.json
    phone = data.get('phone')
    amount = data.get('amount')
    return jsonify({"status": "success", "phone": phone, "amount": amount})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
