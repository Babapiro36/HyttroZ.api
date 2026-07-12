from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
# Hugging Face API anahtarın
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer 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"}

@app.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.json
    mesaj = data.get('mesaj', '')
    payload = {"inputs": mesaj}
    response = requests.post(API_URL, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    # Render'ın portunu otomatik alması için os.environ kullanıyoruz
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
